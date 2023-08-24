from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from crypto.models import Deposit, TransactionSettings, Investment, Withdrawal
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


class UserRegisterForm(UserCreationForm):
    """
        Creates User registration form for signing up.
    """

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        "name": "email", "class": "input100",
        "placeholder": "Email"
    }
    ),
        help_text='Required. Input a valid email address.'
    )
    password1 = forms.CharField(label="Password",
    widget=forms.PasswordInput(attrs={
        "name": "password", "class": "input100",
        "placeholder": "Password"
    }
    ),
    )

    password2 = forms.CharField(label="Confirm Password",
                                help_text=_(
                                    "Enter the same password as before, for verification."),
    widget=forms.PasswordInput(attrs={
        "name": "Confirm Password", "class": "input100",
        "placeholder": "Confirm Password"
    }

    ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {

            "username": forms.TextInput(attrs={
                "name": "username", "class": "input100",
                "placeholder": "Username"
            }),
        }

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class DepositForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'placeholder': 'Enter amount to deposit'})
        self.fields['asset'].widget.attrs.update({'placeholder': 'Select an asset'})

        for field_name, field in self.fields.items():
            field.required = True

        transaction_settings = get_object_or_404(TransactionSettings, pk=1)
        min_deposit = transaction_settings.minimum_deposit
        amount_field = self.fields['amount']
        amount_field.validators.append(MinValueValidator(min_deposit))
    class Meta:
        model = Deposit
        fields = ('amount', 'asset')

class InvestmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'placeholder': 'Enter amount to invest'})
        self.fields['account'].widget.attrs.update({'placeholder': 'Select an account'})
        for field_name, field in self.fields.items():
            field.required = True
        amount_field = self.fields['amount']
        amount_field.validators.append(MinValueValidator(0))
    class Meta:
        model = Investment
        fields = ('amount', 'account')

class WithdrawalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'placeholder': 'Enter amount to invest'})
        self.fields['asset'].widget.attrs.update({'placeholder': 'Select an asset'})
        self.fields['wallet_address'].widget.attrs.update({'placeholder': 'Enter wallet address'})
        self.fields['account'].widget.attrs.update({'placeholder': 'Select an account'})

        for field_name, field in self.fields.items():
            field.required = True
        amount_field = self.fields['amount']
        amount_field.validators.append(MinValueValidator(0))
    class Meta:
        model = Withdrawal
        fields = ('amount', 'asset', 'wallet_address', 'account')