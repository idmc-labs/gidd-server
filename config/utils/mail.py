from django.conf import settings
from django.template import loader

from django.core.mail import EmailMultiAlternatives


def base_send_mail(
    subject_template_name,
    email_html_template_name,
    email_text_template_name,
    context,
    from_email,
    to_email,
):
    """
    Send a django.core.mail.EmailMultiAlternatives to `to_email`.
    Renders provided templates and send it to to_email
    Low level, Don't use this directly
    """
    # Subject
    subject = ''.join(
        # Email subject *must not* contain newlines
        loader.render_to_string(
            subject_template_name,
            context,
        ).splitlines()
    )
    # Body
    html_content = loader.render_to_string(email_html_template_name, context)
    text_content = loader.render_to_string(email_text_template_name, context)
    # Email message
    email_message = EmailMultiAlternatives(
        subject,
        text_content,  # Plain text
        from_email,
        [to_email],
    )
    # HTML
    email_message.attach_alternative(html_content, "text/html")
    # Send email
    email_message.send()


def send_mail(
    subject_template_name,
    email_html_template_name,
    email_text_template_name,
    user,
    context=None,
):
    """
    A generic send mail function
    - With default context values
    - Single receipient
    """
    if context is None:
        context = {}

    context.update({
        'domain': settings.APP_DOMAIN,
        'user': user,
    })

    base_send_mail(
        subject_template_name,
        email_html_template_name,
        email_text_template_name,
        context,
        settings.DEFAULT_FROM_EMAIL,
        user.username,
    )


def send_password_reset_mail(user, context=None):
    send_mail(
        'email/password_reset/subject.txt',
        'email/password_reset/body.html',
        'email/password_reset/body.txt',
        user,
        context,
    )
