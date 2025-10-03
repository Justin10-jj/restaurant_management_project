import string
import secrets
from.models import coupon




def generate_coupon_code(length=10):

    characters=string.ascii__upparcase+string.digits

    while True:
        code=''.join(secrets.choice(characters)for _ in range(length)
        if not coupon.objects.filter(code=code).exists():
            return code


logger=logging.getLogger(__name__)

def send_order_confirmation_email(order_id,customer_email,customer_name,total_amound):
    message=(f"HELLO{customer_name},\n\n"
    f"Thanku You For your Order\n\n"
    f"Order ID:{order_id}\n")

    from_email=settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(subject,message,from_email,[customer_email])
        logger.info(f"ordwer confirmation email sent to {customer_email} for order#{order_id}")
        return("success":True,"message":"Email send successfully")
    except BadHeaderError:
        logger.error("invalid header found while sending email")
        return{"success":False,"message":"invalid header found"}

    except SMTPException as e:
        logger.error(f"SMTP error while sending email:{e}")
        return {"sucess":False,"message":f"SMPT eroor"}



def get_daily_sales_total(date):
    result=Order.objects.filter(create_at__date=date).aggregate(total_sum=sum('total_price'))
    return result['total_sum']or 0