from django.conf import settings


def gidd(request):
    return {
        'request': request,
        'GIDD_ENVIRONMENT': settings.GIDD_ENVIRONMENT,
        'HCAPTCHA_SITE_KEY': settings.HCAPTCHA_SITE_KEY,
    }
