from typing import Any, Dict
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from crypto.models import Deposit, Investment, Withdrawal, Asset, TransactionSettings, MainAccount, ReferralAccount, ProfitAccount
from crypto.forms import DepositForm, InvestmentForm, WithdrawalForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
import random
import string
from decimal import Decimal
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.validators import MinValueValidator
def random_alphanumeric_string():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            # string.digits,
            k=10
        )
    )

class DashboardHome(LoginRequiredMixin,TemplateView):
    template_name = 'userdashboard/dashboard.html'
    login_url = "auth_app:login"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(DashboardHome, self).get_context_data(**kwargs)

        transaction_settings = get_object_or_404(TransactionSettings, pk=1)
        starting_balance = transaction_settings.starting_account_balance
        # Getting the main account balance
        main_account = MainAccount.objects.filter(profile=self.request.user.account)
        if main_account.aggregate(Sum('amount'))['amount__sum'] == None:
            account_balance = starting_balance
        else:
            account_balance = main_account.aggregate(Sum('amount'))['amount__sum']+starting_balance
        # Getting the profit account balance
        profit_account = ProfitAccount.objects.filter(profile=self.request.user.account)
        profit_balance = profit_account.aggregate(Sum('amount'))['amount__sum'] or 0
        # Getting the referral account balance
        referral_account = ReferralAccount.objects.filter(profile=self.request.user.account)
        referral_balance = referral_account.aggregate(Sum('amount'))['amount__sum'] or 0

        # Getting Total withdrawal
        withdrawals = Withdrawal.objects.filter(profile=self.request.user.account)
        total_withdrawal = withdrawals.count()
        # Getting Total Investment
        investments = Investment.objects.filter(profile=self.request.user.account)
        total_investment = investments.count()
        # Getting Pending Deposit
        pending_deposits = Deposit.objects.filter(profile=self.request.user.account, status='Pending')
        total_pending_deposits = pending_deposits.count()
        # Getting Pending Withdrawal
        pending_withdrawals= Withdrawal.objects.filter(profile=self.request.user.account, status='Pending')
        total_pending_withdrawals = pending_withdrawals.count()
        # Getting Completed Deposit
        completed_deposits = Deposit.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_deposits = completed_deposits.count()
        completed_deposit_balance = completed_deposits.aggregate(Sum('amount'))['amount__sum'] or 0
        # Getting Completed Investment
        completed_investments = Investment.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_investments = completed_investments.count()
        completed_investment_balance = completed_investments.aggregate(Sum('amount'))['amount__sum'] or 0
        # Getting Completed Withdrawal
        completed_withdrawals = Withdrawal.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_withdrawals = completed_withdrawals.count()
        # Getting Cancelled Investment
        cancelled_investments = Investment.objects.filter(profile=self.request.user.account, status='Cancelled')
        total_cancelled_investments = cancelled_investments.count()
        # Getting Ongoing Investment
        ongoing_investments = Investment.objects.filter(profile=self.request.user.account, status='Ongoing')
        total_ongoing_investments = ongoing_investments.count()

        # Getting the main account balance
        main_account = MainAccount.objects.filter(profile=self.request.user.account)
        main_account_balance = main_account.aggregate(Sum('amount'))['amount__sum'] or 0
        account_balance = main_account_balance+starting_balance+completed_deposit_balance-completed_investment_balance
        
        context['account_balance'] = account_balance
        context['profit_balance'] = profit_balance
        context['referral_balance'] = referral_balance
        context['total_withdrawal'] = total_withdrawal
        context['total_investment'] = total_investment
        context['total_pending_deposits'] = total_pending_deposits
        context['total_pending_withdrawals'] = total_pending_withdrawals
        context['total_completed_deposits'] = total_completed_deposits
        context['total_completed_investments'] = total_completed_investments
        context['total_cancelled_investments'] = total_cancelled_investments
        context['total_ongoing_investments'] = total_ongoing_investments
        context['total_completed_withdrawals'] = total_completed_withdrawals
        return context 

class DepositListView(LoginRequiredMixin,ListView):
    model = Deposit
    template_name = 'userdashboard/deposit_list.html'
    login_url = "auth_app:login"

class DepositCreateView(LoginRequiredMixin,CreateView):
    model = Deposit
    form_class = DepositForm
    template_name = 'userdashboard/new_deposit.html'
    success_url = reverse_lazy('crypto:deposit_list')
    redirect_field_name = "redirect_to"
    login_url = "auth_app:login"

    def form_valid(self, form):
        form.instance.profile = self.request.user.account
        return super().form_valid(form)
    
class DepositDetailView(LoginRequiredMixin, DetailView):
    model = Deposit
    template_name = 'userdashboard/deposit_detail.html'
    login_url = "auth_app:login"
    

class InvestmentListView(LoginRequiredMixin, ListView):
    model = Investment
    template_name = 'userdashboard/investment_list.html'
    login_url = "auth_app:login"

class InvestmentDetailView(LoginRequiredMixin, DetailView):
    model = Investment
    template_name = 'userdashboard/investment_detail.html'
    login_url = "auth_app:login"

class InvestmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Investment
    form_class = InvestmentForm
    success_url = reverse_lazy('crypto:investment_list')
    template_name = 'userdashboard/new_investment.html'
    redirect_field_name = "redirect_to"
    success_message = "Investment was created successfully"
    login_url = "auth_app:login"

    def form_valid(self, form):
        form.instance.profile = self.request.user.account
        return super().form_valid(form)
    
    def form_invalid(self, form):
        amount_field = form.cleaned_data['amount']
        # user = self.instance.user
        transaction_settings = get_object_or_404(TransactionSettings, pk=1)
        starting_balance = transaction_settings.starting_account_balance
        # Getting Completed Deposit
        completed_deposits = Deposit.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_deposits = completed_deposits.count()
        completed_deposit_balance = completed_deposits.aggregate(Sum('amount'))['amount__sum'] or 0
        # Getting Completed Investment
        completed_investments = Investment.objects.filter(profile=self.request.user.account, status='Completed')
        total_completed_investments = completed_investments.count()
        completed_investment_balance = completed_investments.aggregate(Sum('amount'))['amount__sum'] or 0
        # Getting the main account balance
        main_account = MainAccount.objects.filter(profile=self.request.user.account)
        main_account_balance = main_account.aggregate(Sum('amount'))['amount__sum'] or 0
        account_balance = main_account_balance+starting_balance+completed_deposit_balance-completed_investment_balance
        # amount_field.validators.append(MinValueValidator(account_balance))

        if amount_field > account_balance:
            form.add_error('amount', 'Your account is low. Kindly fund your account')
            return self.form_invalid(form)

        return super().form_valid(form)

class WithdrawalListView(LoginRequiredMixin, ListView):
    model = Withdrawal
    template_name = 'userdashboard/withdrawal_list.html'
    login_url = "auth_app:login"

class WithdrawalDetailView(LoginRequiredMixin, DetailView):
    model = Withdrawal
    template_name = 'userdashboard/withdrawal_detail.html'
    login_url = "auth_app:login"

class WithdrawalCreateView(LoginRequiredMixin, CreateView):
    model = Withdrawal
    form_class = WithdrawalForm
    success_url = reverse_lazy('crypto:withdrawal_list')
    template_name = 'userdashboard/new_withdrawal.html'
    redirect_field_name = "redirect_to"
    login_url = "auth_app:login"

    def form_valid(self, form):
        form.instance.profile = self.request.user.account
        return super().form_valid(form)