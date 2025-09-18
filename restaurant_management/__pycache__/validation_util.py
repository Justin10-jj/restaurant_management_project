import logging
from email.utils import parseaddr

logger=looging.getLogger(__name__)
def is_valid_email(email:str) ->bool:
    try:
        if not email or"@" not in email:
            return False
        name,addr=parseaddr(email)

        if "@" not in addr:
            return False 

        local_part or not domain=addr.rsplit("@",1)

        if not local_part or not domain:
            return False
        
        if "." not in domain:
            return False

        return True

    except Exception as e:
        logger.error(f"Error validation email'{email}':{e}")
        
        return False