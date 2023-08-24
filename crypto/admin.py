from django.contrib import admin
from crypto import models
# Register your models here.

@admin.register(models.Deposit)
class DepositAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount', 'asset',
              'status')
    list_display = ('profile', 'reference', 'amount','asset',
              'date_initiated', 'status')
    list_filter = ("status", 'profile', 'date_initiated')
    empty_value_display = '-None-'

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'photo', 'phone_number',
              'slug', 'address', 'country', 'date_of_birth', 'email_confirmed')
    list_display = ('user', 'photo', 'phone_number',
              'reference', 'slug', 'address', 'country', 'date_of_birth', 'email_confirmed', 'date_created')
    prepopulated_fields = {'slug': ('user',)}
    empty_value_display = '-None-'

@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    fields = ('asset_icon', 'asset_name', 'asset_abbr')
    list_display = ('asset_icon', 'asset_name', 'asset_abbr')
    empty_value_display = '-None-'

@admin.register(models.Investment)
class InvestmentAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount', 'roi', 'current_profit', 'account', 'status')
    list_display = ('profile', 'reference', 'amount', 'roi', 'current_profit', 'account', 'date_initiated', 'status')
    empty_value_display = '-None-'

@admin.register(models.Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount', 'asset', 'wallet_address', 'account', 'status')
    list_display = ('profile', 'reference', 'amount','asset', 'wallet_address', 'account', 'date_requested', 'status')
    empty_value_display = '-None-'

@admin.register(models.MainAccount)
class MainAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')
    empty_value_display = '-None-'

@admin.register(models.ProfitAccount)
class ProfitAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')
    empty_value_display = '-None-'

@admin.register(models.ReferralAccount)
class ReferralAccountAdmin(admin.ModelAdmin):
    fields = ('profile', 'amount')
    list_display = ('profile', 'amount', 'date_initiated')
    empty_value_display = '-None-'

@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ('site_name', 'site_logo')
    list_display = ('site_name', 'site_logo')
    empty_value_display = '-None-'

@admin.register(models.TransactionSettings)
class TransactionSettings(admin.ModelAdmin):
    fields = ('minimum_deposit',)
    list_display = ('minimum_deposit',)
    empty_value_display = '-None-'