from django.urls import path
from .views import *

urlpatterns = [
    path("order/<int:pk>/total/",order_total_view,name="order-total"),
    path("order/<int:pk>/update-status/",OrderStatusUpdateView.as_view(),ame="order-status-update"),
    path("api/sales/daily/",DailySalesAPIView.as_view(),name="daily_sales_api"),
]