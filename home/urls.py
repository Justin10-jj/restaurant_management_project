from django.urls import path
from .views import *

urlpatterns = [
    path=('daily-specials/',DailySpecialListView.as_View(),name='daily-specials'),
    path=("api/tables/availabile/",AvailaibleTableAPIView.as_view(),name="availabile_table_api"),
    path("api/tables/<int:pk>",TableDetailAPIView.as_View(),name="table_detail_api"),
    path("api/restaurant/status/",RestaurantStatusAPIView.as_view(),name="restaurant_status"),
    path('',include(router.urls)),
]