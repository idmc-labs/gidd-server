from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.translation import gettext
from django.db import transaction

from .tasks import send_email


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            user = User.objects.filter(email=data).first()
            if user:
                subject = "Password Reset Requested"
                message = gettext(
                    "We received a request to reset the password for your account for this email address."
                    "To initiate the password reset process for your account, click the link below."
                )
                context = {
                    "message": message,
                    "email": user.email,
                    'domain': settings.DOMAIN_URL,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
                print(context)
                transaction.on_commit(lambda: send_email.delay(
                    subject, message, [user.email, ], html_context=context
                ))
                return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})
