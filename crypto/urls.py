from django.urls import path
from django.contrib.auth import views as auth_views
from .views import dashboard
app_name = 'crypto'

urlpatterns = [
    path(route='', view=dashboard.DashboardHome.as_view(), name='dashboard'),
    path(route='deposit/list', view=dashboard.DepositListView.as_view(), name='deposit_list'),
    path(route='deposit/<str:slug>', view=dashboard.DepositDetailView.as_view(), name='deposit_detail'),
    path(route='investment/list', view=dashboard.InvestmentListView.as_view(), name='investment_list'),
    path(route='investment/<str:slug>', view=dashboard.InvestmentDetailView.as_view(), name='investment_detail'),
    path(route='withdrawal/list', view=dashboard.WithdrawalListView.as_view(), name='withdrawal_list'),
    path(route='withdrawal/<str:slug>', view=dashboard.WithdrawalDetailView.as_view(), name='withdrawal_detail'),
    path(route='new/deposit', view=dashboard.DepositCreateView.as_view(), name='new_deposit'),
    path(route='new/investment', view=dashboard.InvestmentCreateView.as_view(), name='new_investment'),
    path(route='new/withdrawal', view=dashboard.WithdrawalCreateView.as_view(), name='new_withdrawal'),

]