from django.urls import path

from .views import (
    StoreView,  
)

app_name="marketplace"

urlpatterns = [

    path('products/', StoreView.as_view(), name="products"),


]