from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .tokens import account_activation_token
from django.http.response import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView,
                                        PasswordResetCompleteView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView, LogoutView)
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.urls import reverse_lazy
from auth_app.forms import UserRegisterForm

from crypto.models import SiteSettings
from django.shortcuts import get_object_or_404
site_setting = get_object_or_404(SiteSettings, pk=1)
company_email = site_setting.company_email
# company_email = 'jetticons@gmail.com'

class UserLoginView(View):
    """
     Logs user into dashboard.
    """
    template_name = 'authentication/login.html'
    context_object = {"login_form": AuthenticationForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            
            login(request, user)
            messages.success(request, f"Login Successful ! "
                                f"Welcome {user.username}.")
            return redirect('crypto:dashboard')

        else:
            messages.error(request,
                           f"Please enter a correct username and password. Note that both fields may be case-sensitive."
                           )
            return render(request, self.template_name, self.context_object)
        


class LogoutView(LogoutView):
    template_name = 'authentication/logged_out.html'
    
class PasswordResetView(PasswordResetView):
    template_name = 'authentication/pwd_reset_form.html'
    email_template_name = "authentication/email_text/password_reset_email.html"
    from_email = company_email
    subject_template_name = "authentication/email_text/password_reset_subject.txt"
    success_url = reverse_lazy("auth_app:password_reset_done")

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html' 

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy("auth_app:password_reset_complete")

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'

class PasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password_change_form.html'
    success_url = reverse_lazy("auth_app:password_change_done")

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'




UserModel = get_user_model()


class UserRegisterView(View):
    """
      View to let users register
    """
    template_name = 'authentication/register.html'
    context = {
        "register_form": UserRegisterForm()
    }

    def get(self, request):
        success_message = "Successful"
        self.context['success_message'] = success_message
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('authentication/activate_email.html'
                                       , {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
            }
            )
            from_email = company_email
            to_email = register_form.cleaned_data.get('email')
            print(to_email)
            print(message)
            email = EmailMessage(
                mail_subject, message, from_email, to=[to_email]
            )
            email.send()

            return HttpResponseRedirect(reverse_lazy('auth_app:email_verification_confirm'))

        else:
            messages.error(request, "Please provide valid information.")
            # Redirect user to register page
            return render(request, self.template_name, self.context)

    def get_success_url(self):
        return reverse('main:home')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(
            request, f'Hi {user.username}, your registration was successful!! .')
        return reverse('main:home')
    else:
        return reverse_lazy('auth_app:email_verification_invalid')


class EmailVerificationConfirm(TemplateView):
    template_name = 'authentication/email_verification_confirm.html'


class EmailVerificationInvalid(TemplateView):
    template_name = 'authentication/email_verification_invalid.html'