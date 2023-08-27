from django.contrib import admin
from crypto import models
# Register your models here.

@admin.register(models.Deposit)
class DepositAdmin(admin.ModelAdmin):
    fields = ('profile', 'reference', 'amount', 'asset',
              'status', 'slug')
    list_display = ('profile', 'reference', 'amount','asset',
              'date_initiated', 'status', 'slug')
    list_filter = ("status", 'profile', 'date_initiated')
    empty_value_display = '-None-'
    prepopulated_fields = {'slug': ('reference',)}

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'photo', 'phone_number',
              'slug', 'address', 'country', 'date_of_birth', 'email_confirmed')
    list_display = ('user', 'photo', 'phone_number',
              'reference', 'slug', 'address', 'country', 'date_of_birth', 'email_confirmed', 'date_created')
    prepopulated_fields = {'slug': ('user',)}
    empty_value_display = '-None-'
    # prepopulated_fields = {'slug': ('reference',)}

@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    fields = ('asset_icon', 'asset_name', 'asset_abbr')
    list_display = ('asset_icon', 'asset_name', 'asset_abbr')
    empty_value_display = '-None-'

@admin.register(models.Investment)
class InvestmentAdmin(admin.ModelAdmin):
    fields = ('profile', 'package','reference', 'amount', 'account', 'status', 'slug')
    list_display = ('profile','package', 'reference', 'amount',  'account', 'date_initiated', 'status', 'slug')
    prepopulated_fields = {'slug': ('reference',)}

@admin.register(models.Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    fields = ('profile','reference', 'amount', 'asset', 'wallet_address', 'account', 'status', 'slug')
    list_display = ('profile', 'reference', 'amount','asset', 'wallet_address', 'account', 'date_requested', 'status', 'slug')
    prepopulated_fields = {'slug': ('reference',)}

@admin.register(models.MainAccount)
class MainAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')

@admin.register(models.ProfitAccount)
class ProfitAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')

@admin.register(models.ReferralAccount)
class ReferralAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')
    empty_value_display = '-None-'

@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ('site_name', 'site_logo', 'company_email')
    list_display = ('site_name', 'site_logo', 'company_email')
    empty_value_display = '-None-'

@admin.register(models.TransactionSettings)
class TransactionSettings(admin.ModelAdmin):
    fields = ('minimum_deposit','company_wallet_address', 'starting_account_balance')
    list_display = ('minimum_deposit','company_wallet_address', 'starting_account_balance')
    empty_value_display = '-None-'

@admin.register(models.PackageType)
class PackageTypeAdmin(admin.ModelAdmin):
    fields = ('package_name',)
    list_display = ('package_name',)
    empty_value_display = '-None-'

@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):
    fields = ('package_type','roi', 'min_investment', 'max_investment', 'duration', 'current_no_of_return', 'no_of_return')
    list_display = ('package_type', 'roi', 'min_investment', 'max_investment', 'duration', 'current_no_of_return', 'no_of_return')
    empty_value_display = '-None-'