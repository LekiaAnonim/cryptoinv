from django.urls import path
from django.contrib.auth import views as auth_views
from .views import authentication, dashboard
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

    # Signup and SignIn URL
    path(
        route='signup',
        view=authentication.UserRegisterView.as_view(),
        name='signup'
    ),
    path(
        route='email-verification-confirm',
        view=authentication.EmailVerificationConfirm.as_view(),
        name='email_verification_confirm'
    ),
    path(
        route='email-verification/invalid-link',
        view=authentication.EmailVerificationInvalid.as_view(),
        name='email_verification_invalid'
    ),
    path(
        route='login',
        view=authentication.UserLoginView.as_view(),
        name='login'
    ),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # Reset Password URLS

    path(
        route='reset-password',
        view=authentication.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path('password-reset/done/', authentication.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         authentication.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset_complete/done/', authentication.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('password-change', authentication.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', authentication.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('activate/<uidb64>/<token>/',
         authentication.activate, name='activate'),
]