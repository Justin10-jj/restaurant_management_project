from django.urls import path
from .views import *

urlpatterns = [
    path=('daily-specials/',DailySpecialListView.as_View(),name='daily-specials'),
]