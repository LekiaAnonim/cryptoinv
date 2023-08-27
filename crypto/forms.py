from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from crypto.models import Deposit, TransactionSettings, Investment, Withdrawal, MainAccount
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Sum



    
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
        fields = ('profile','amount', 'asset')

class InvestmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'placeholder': 'Enter amount to invest'})
        self.fields['package'].widget.attrs.update({'placeholder': 'Select package'})
        self.fields['account'].widget.attrs.update({'placeholder': 'Select an account'})
        for field_name, field in self.fields.items():
            field.required = True
        amount_field = self.fields['amount']
        amount_field.validators.append(MinValueValidator(0))

        transaction_settings = get_object_or_404(TransactionSettings, pk=1)
        starting_balance = transaction_settings.starting_account_balance
        # Getting Completed Deposit
        completed_deposits = Deposit.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_deposits = completed_deposits.count()
        completed_deposit_balance = completed_deposits.aggregate(Sum('amount'))['amount__sum']
        # Getting Completed Investment
        completed_investments = Investment.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_investments = completed_investments.count()
        completed_investment_balance = completed_investments.aggregate(Sum('amount'))['amount__sum']
        # Getting the main account balance
        main_account = MainAccount.objects.filter(profile=self.request.user.account)
        main_account_balance = main_account.aggregate(Sum('amount'))['amount__sum'] or 0
        account_balance = main_account_balance+starting_balance+completed_deposit_balance-completed_investment_balance
        amount_field.validators.append(MinValueValidator(account_balance))

    class Meta:
        model = Investment
        fields = ('profile','amount', 'package', 'account')

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
        fields = ('profile','amount', 'asset', 'wallet_address', 'account')