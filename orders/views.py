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