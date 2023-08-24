from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from crypto.models import TransactionSettings, SiteSettings, Asset
from django.shortcuts import get_object_or_404

def base_data(request):
    data = {}
    transaction_settings = get_object_or_404(TransactionSettings, pk=1)
    site_setting = get_object_or_404(SiteSettings, pk=1)
    assets = Asset.objects.all()
    data['transaction_settings'] = transaction_settings
    data['site_setting'] = site_setting
    data['assets'] = assets
    return data