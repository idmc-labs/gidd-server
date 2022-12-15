from django.conf import settings
import requests
from dataclasses import asdict

HCAPTCHA_VERIFY_URL = 'https://hcaptcha.com/siteverify'

# FOR TEST: https://docs.hcaptcha.com/#test-key-set-publisher-account


def validate_hcaptcha(captcha):
    if not captcha:
        return False

    data = {
        'secret': settings.HCAPTCHA_SECRET,
        'response': captcha,
    }
    response = requests.post(url=HCAPTCHA_VERIFY_URL, data=data)

    response_json = response.json()
    return response_json['success']


def get_values_list_from_dataclass(data_class):
    if data_class:
        return asdict(data_class)
    return {}
