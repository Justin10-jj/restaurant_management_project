from django.urls import path
from .views import *

urlpatterns = [
    path=('daily-specials/',DailySpecialListView.as_View(),name='daily-specials'),
    path=("api/tables/availabile/",AvailaibleTableAPIView.as_view(),name="availabile_table_api"),
]