from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from crypto.models import Deposit, Investment, Withdrawal, Asset, TransactionSettings
from crypto.forms import DepositForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
import random
import string
from decimal import Decimal
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
def random_alphanumeric_string():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            # string.digits,
            k=10
        )
    )

class DashboardHome(TemplateView):
    template_name = 'userdashboard/dashboard.html'

class DepositListView(ListView):
    model = Deposit
    template_name = 'userdashboard/deposit_list.html'

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'userdashboard/new_deposit.html'
    success_url = reverse_lazy('crypto:deposit_list')
    redirect_field_name = "redirect_to"
    
class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'userdashboard/deposit_detail.html'
    

class InvestmentListView(ListView):
    model = Investment
    template_name = 'userdashboard/investment_list.html'

class InvestmentDetailView(DetailView):
    model = Investment
    template_name = 'userdashboard/investment_detail.html'

class InvestmentCreateView(SuccessMessageMixin, CreateView):
    model = Investment
    fields = ('amount', 'account')
    success_url = reverse_lazy('crypto:investment_list')
    template_name = 'userdashboard/new_investment.html'
    redirect_field_name = "redirect_to"
    success_message = "Investment was created successfully"

class WithdrawalListView(ListView):
    model = Withdrawal
    template_name = 'userdashboard/withdrawal_list.html'

class WithdrawalDetailView(DetailView):
    model = Withdrawal
    template_name = 'userdashboard/withdrawal_detail.html'

class WithdrawalCreateView(CreateView):
    model = Withdrawal
    fields = ('amount', 'asset', 'wallet_address', 'account')
    success_url = reverse_lazy('crypto:withdrawal_list')
    template_name = 'userdashboard/new_withdrawal.html'
    redirect_field_name = "redirect_to"