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


logger=logging.getLogger(__name__)
def update_order_status(order_id,new_status):

    try:
        oredr=Order.objects.grt(id=order_id)
        old_status=order.new_status
        logger.info(f"Attempting to update Order #{order_id}from '{order_status}' to '{new_status}.")
        oredr.status=new_status
        oredr.save(update_fields=['status'])

        logger.info(f"oredr"{order_id} status upadted successfully to '{new_status}')
        return oredr


    except ObjectDoesNotExist:
        logger.error(f"order with ID{order_id} not found.")
        return None

    except Exception as e:
        logger.exception(f"Error updating order{oredr_id}:{e}")
        return None 


def calculate_order_total(order_items):
    if not order_items or not isinstance (order_items,list):
        return 0.0
    total=0.0
    for item in order_items:
        quantity=item.get('quantity',0)
        price=item.get('price',0)
        try:
            total+=float(quantity)*float(price)
        except(TypeError,ValueError):
            continue
    return round(total,2)

def claculate_discountamound(order_total,discountt_percentage):
    try:
        order_total=float(oredr_total)
        discountt_percentage=float(discountt_percentage)
        if oredr_total<0 or discountt_percentage<0:
            raise ValueError("value ,ust be non negative")
        discount_amound=oredr_total*(discountt_percentage/100)
        return round(discount_amound,2)
    except(ValueError,TypeError):
        return 0.0