from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from config.utils.mail import send_password_reset_mail
from django.contrib import messages


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            email = password_reset_form.cleaned_data['email']
            user = User.objects.filter(email__iexact=email).first()
            if user:
                context = {
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
                send_password_reset_mail(user, context)
                messages.success(request, "Please check your email for password reset link.")
                return redirect("password_reset")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="email/password_reset/password_reset.html",
        context={"password_reset_form": password_reset_form}
    )
