import string
import secrets
from.models import coupon




def generate_coupon_code(length=10):

    characters=string.ascii__upparcase+string.digits

    while True:
        code=''.join(secrets.choice(characters)for _ in range(length)
        if not coupon.objects.filter(code=code).exists():
            return code