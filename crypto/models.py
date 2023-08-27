from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from decimal import Decimal
from datetime import datetime, timedelta
import random
import string


def random_alphanumeric_string():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            # string.digits,
            k=10
        )
    )
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, related_name="account", on_delete=models.CASCADE)
    photo = CloudinaryField('image', null=True, blank=True)
    phone_number = models.CharField(
        max_length=12, null=True, help_text="Enter your State or Phone Number")
    reference = models.CharField(default= random_alphanumeric_string(), max_length=10, null=True, editable=False, unique=True)
    slug = models.SlugField(null=True,  max_length=500)
    address = models.CharField(
        max_length=500, blank=True, null=True, help_text="Enter your House address")
    country = models.CharField(
        max_length=100, help_text="Enter your Country (e.g. Nigeria)", null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"@{self.user.username}-{self.reference}"

    def get_absolute_url(self):
        return reverse('crypto:profile_detail', kwargs={'username': self.user.username.lower(), 'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name, allow_unicode=True)
        self.last_name = self.user.last_name
        super(Profile, self).save(*args, **kwargs)

class Asset(models.Model):
    asset_icon = CloudinaryField('image', null=True, blank=True)
    asset_name = models.CharField(max_length=50, null=True)
    asset_abbr = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.asset_name}"
    
class PackageType(models.Model):
    package_name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.package_name
class Package(models.Model):
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE, null=True)
    min_investment = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    max_investment = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    duration = models.IntegerField(null=True)
    current_no_of_return = models.IntegerField(null=True)
    no_of_return = models.IntegerField(null=True)
    # profit_per_return = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    roi = models.DecimalField(decimal_places=1, max_digits=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.package_type.package_name}({self.min_investment} - {self.max_investment})"

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, null=True, blank=True)
    site_logo = CloudinaryField('image', null=True, blank=True)
    company_email = models.EmailField(max_length=500, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Site Settings'

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('There can be only one SiteSettings instance')
        return super(SiteSettings, self).save(*args, **kwargs)

class TransactionSettings(models.Model):
    minimum_deposit = models.DecimalField(decimal_places=2, default=100, max_digits=100, null=True, blank=True)
    company_wallet_address = models.CharField(max_length=500, null=True)
    starting_account_balance = models.DecimalField(decimal_places=2, default=100, max_digits=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transaction Settings'
    def save(self, *args, **kwargs):
        if not self.pk and TransactionSettings.objects.exists():
        # if you'll not check for self.pk 
        # then error will also be raised in the update of exists model
            raise ValidationError('There can be only one TransactionSettings instance')
        return super(TransactionSettings, self).save(*args, **kwargs)
    
class Deposit(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='deposit_user')
    reference = models.CharField(default=random_alphanumeric_string(), max_length=50, null=True, editable=True)
    slug = models.SlugField(null=True,  max_length=500)
    amount = models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    asset = models.ForeignKey(Asset, null=True, on_delete=models.SET_NULL, related_name='deposit_asset')
    date_initiated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(null=True,
        max_length=100, choices=STATUS_CHOICES, default='Completed')
    
    def __str__(self):
        return f"{self.profile.user.username}-{self.reference}-{self.date_initiated}-{self.amount}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.reference, allow_unicode=True)
        super(Deposit, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('crypto:deposit_detail', kwargs={'slug': self.slug})

class Investment(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='invest_user')
    reference = models.CharField(default=random_alphanumeric_string(), max_length=50, null=True, editable=True)
    slug = models.SlugField(null=True,  max_length=500)
    amount =  models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    package = models.ForeignKey(Package, null=True, on_delete=models.SET_NULL)
    date_initiated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(null=True,
        max_length=100, choices=STATUS_CHOICES, default='Completed')
    
    ACCOUNT_CHOICES = (
        ('account_balance', 'Account Balance'),
    )
    account = models.CharField(null=True,
        max_length=100, choices=ACCOUNT_CHOICES, default='Account Balance')
    
    def __str__(self):
        return f"{self.profile.user.username}-{self.reference}-{self.date_initiated}-{self.amount}-{self.pk}"
    
    @property
    def profit_per_return(self):
        profit = (self.package.roi*self.amount)/100
        return profit
    
    @property
    def current_profit(self):
        profit = (self.package.current_no_of_return*self.package.roi*self.amount)/100
        return profit
    
    @property
    def expected_profit(self):
        profit = (self.package.no_of_return*self.package.roi*self.amount)/100
        return profit
    
    @property
    def next_date_of_return(self):
        next_date = self.date_initiated + timedelta( days = self.package.duration)
        return next_date
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.reference, allow_unicode=True)
        super(Investment, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('crypto:investment_detail', kwargs={'slug': self.slug})
    

class Withdrawal(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='withdrawal_user')
    reference = models.CharField(default=random_alphanumeric_string(), max_length=50, null=True, editable=True)
    slug = models.SlugField(null=True,  max_length=500)
    amount=  models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    asset = models.ForeignKey(Asset, null=True, on_delete=models.SET_NULL, related_name='withdrawal_asset')
    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    date_requested = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(null=True,
        max_length=100, choices=STATUS_CHOICES, default='Completed')
    
    ACCOUNT_CHOICES = (
        ('profit balance', 'Profit Balance'),
        ('referral balance', 'Referral Balance'),
    )
    account = models.CharField(null=True,
        max_length=100, choices=ACCOUNT_CHOICES, default='Profit Balance')
    
    def __str__(self):
        return f"{self.profile.user.username}-{self.reference}-{self.date_requested}-{self.amount}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.reference, allow_unicode=True)
        super(Withdrawal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('crypto:withdrawal_detail', kwargs={'slug': self.slug})
    
class MainAccount(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='account_user')
    amount=  models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    date_initiated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.user.username}-{self.date_initiated}-{self.amount}"
    
class ProfitAccount(models.Model):
    profile = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL, related_name='profit_user')
    amount=  models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    date_initiated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.user.username}-{self.date_initiated}-{self.amount}"
    
class ReferralAccount(models.Model):
    profile = models.ForeignKey(Profile,  null=True, on_delete=models.SET_NULL, related_name='referral_user')
    amount=  models.DecimalField(decimal_places=2, max_digits=100, null=True, default=0)
    date_initiated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.profile.user.username}-{self.date_initiated}-{self.amount}"