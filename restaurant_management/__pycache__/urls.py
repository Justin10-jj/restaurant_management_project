from django.urls import path
from.import views

urlpatterns=[
    path('confirmation',views.order_confirmation,name='order_confirmation'),
]