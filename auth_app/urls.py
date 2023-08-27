from django.urls import path
from django.contrib.auth import views as auth_views
from .views import authentication
app_name = 'auth_app'

urlpatterns = [

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
    path('logout', authentication.LogoutView.as_view(), name='logout'),

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