import random
from django.conf import settings
from .models import PhoneVerification

def generate_code() -> str:
    return f'{random.randint(0, 999_999):06d}'

def send_verification_sms(phone: str, code: str):
    if settings.DEBUG:
        print(f'[SMS MOCK] Код для {phone}: {code}')
    else:
        raise NotImplementedError('Подключите SMS-провайдера для начала работы')

def create_verification(phone: str) -> PhoneVerification:
    code = generate_code()
    verification = PhoneVerification.objects.create(phone=phone, code=code)
    send_verification_sms(phone, code)
    return verification

def verify_code(phone: str, code: str) -> bool:
    verification = (
        PhoneVerification.objects
            .filter(phone=phone, code=code, is_used=False)
            .order_by('-created_at')
            .first()
    )

    if verification is None or verification.is_expired():
        return False

    verification.is_used = True
    verification.save()
    return True