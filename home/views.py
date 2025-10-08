from django.shortcuts import render

# Create your views here.

class ContactFormSubmissionView(generic.CreateAPIView):
    queryset=ContactFormSubmission.objects.all()
    serializer_class=ContactFormSubmissionSerializer

    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid()
        serializer.save()
        return Response(
            {"message":"ypur contact form has been submitted successfullt"

            }
        )
    return Response(serializer.error)



class DailySpeciaListView(generics.ListAPIView):
    serializer_class=DailySpecialSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_daily_special=True)


class AvailableTableAPIView(generics.ListAPIView):
    serializer_class=TableSerializer

    def get_queryset(self):
        return Table.objects.filter(is_available=True)


class TableDetailsAPIView(generics.RetrieveAPIView):
    queryset=Table.objects.all()
    serializer_class=TableSerializer 

class RestaurantStatusAPIView(APIView):
    def get(self,request):
        status=is_restaurant_open()
        return Response({"is_open":status})


class MenuCategoryViewSet(Viewsets.MpdelViewSet):
    queryset=MenuCategory.objects.all().order_by('id')
    serializer_class=MenuCategorySerializer
    permission_classes=[permission.IsAuthenticatedOrderReadyOnly]



class UserReviewcreateView(generics.CreateAPIView):
    queryset=UserReview.objects.all()
    serializer_class=UserReviewserializer
    permission_classes=[permission.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MenuItemReviewListView(generics.ListAPIView):
    serializer_class=UserReviewserializer
    permission_classes=[permissions.AllpwAny]

    def get_queryset(self):
        menu_item_id=self.kwargs.get('menu_item_id')
        return Userreview.objects.filter(menu_item_id=menu_item_id).order_by('-review_data')