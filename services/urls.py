from django.urls import path

from .views import (
    ServicesView,
    chooseView,
)

app_name="services"

urlpatterns = [

    path('services/', ServicesView.as_view(), name="services"),

    path('company/', chooseView.as_view(), name="company"),

    
]