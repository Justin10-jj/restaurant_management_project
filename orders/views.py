from django.shortcuts import render

# Create your views here.

def generate_coupon_view(request):
    new_code=generate_coupon_code()
    coupon=coupon.objects.create(code=new,discount=15.00)

    return JsonResponse({
        "message":"coupon generated successfully",
        "coupon_code":coupon_code,
        "discount":str(coupon.discount),    })


class OrderHistoryView(generic.ListAPIView):
    serializer_xlass=OrderSerializer
    permission_classes=[permission.IsAuthentication]

    def get_queryset(self)
    return Order.objects.filter(user=self.request.user).order_by("created_at")



def created_order(request):
    order_id=101
    customer_email="customer@emailexample.com"
    customer_name="john"
    total_amound=49.99

    result=send_order_confirmation_email(order_id,customer_email,customername,total_amound)



    return Response(result)



class OrderDetailView(generics.RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[perimission.IsAuthentication]
    loookup_field="id"



class CancelOrderView(APIView):
    permission_classes=[perimissions.IsAuthentication]
    def delete(self,request,order_id):
        order=get_object_or_404(Order,id=order_id)
        if order.status in["CANCELLED","COMPLETED"]:
            return Response(
                {"error":f"order is already{order.ststus.lower()}."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        order.status="CANCELLED"
        oredr.save()
        return Response(
            {"message":f"order{order.id} has been cancelled"},
        )

class NotifyCustomerView(APIView):
    def post(self,request)
    email=reuest.data.get("email")
    subject=request.data.get("subject","order update")
    message=request.data.get("message","thank you for your rder")
    result=send_email_util(email,subject,message)
    
@api_view['GET']
def order_total(request,pk):
    oredr=Order.objects.get(pk=pk)
    return Response({
        "order_id":oredr.id,
        "customer":order.customer_name,
        "total":str(order.calculate_total())
            })