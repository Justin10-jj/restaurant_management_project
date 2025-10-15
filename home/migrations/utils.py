from django.core.validators import validate_email
from django.core.exceptions import ValidationError 


def is_valid_email(email:str)->bool:


    if not email:
        return False

    try:
        validate_email(email)
        return True
    except ValidationError:
        return False 