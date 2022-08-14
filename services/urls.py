from django.urls import path

from .views import (
    ServicesView,
    chooseView,
    EmpresaDetailView,
    CreateCompanyView,
    CompanyUpdateView
    
)

app_name="services"

urlpatterns = [

    path('services/', ServicesView.as_view(), name="services"),

    path('company/', chooseView.as_view(), name="company"),

    path('company/<slug>/', EmpresaDetailView.as_view(), name="company-detail"),

    path('createCompany/', CreateCompanyView.as_view(), name="create-Company"),

    path('company/<slug>/update/', CompanyUpdateView.as_view(), name="company-update"),




    
]