from django.urls import path
from .views import *

urlpatterns = [
    path("order/<int:pk>/total/",order_total_view,name="order-total"),
]