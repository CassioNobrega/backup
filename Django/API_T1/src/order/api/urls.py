from django.urls import path

from order.api.views import OrdersList

urlpatterns = [
    path('orders/', OrdersList.as_view()),  
]
