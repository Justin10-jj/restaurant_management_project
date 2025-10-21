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


class DailySalesAPIView(APIView):
    def get(self,request):
        today=date.today()
        total_sales=get_daily_sales_total(total)
        return Response({"date":str(today),"total_sales":total_sales})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_oreder_status(request,order_id):
    order=get_order_or_404(Oredr,id=order_id):
    return Response({
        "order_id"order_id,
        "status":oredr.status
    }),status=status.HTTP_200_OK


class OrderStatusView(generics.RetrieveAPIView):
    serilizer_class=OrderStatusSerilizer
    lookup_field='short_id'
    queryset=Order.objects.all()
    def get(slf,request,*args,**kwargs):
        short_id=kwargs.get('short_id')

        try:
            order=Oredr.objects.get(short_id=short_id)
        except Order.DoesNotExist:
            raise NotFound(detail="order not found with the given ID")
        serilizer=self.get_serilizer(order)
        return Response(serilizer.data)