from django.urls import path

from .views import (
    ServicesView,
    chooseView,
    EmpresaDetailView,
    CreateCompanyView,
    CompanyUpdateView,
    ServiceUpdateView,
    ServiceDeleteView,
    ILikeCompany,
    NotLikeCompany,
    ServiceDetailView,
    ServiceSearch,


)

app_name="services"

urlpatterns = [

    path('services/', ServicesView.as_view(), name="services"),

    path('company/', chooseView.as_view(), name="company"),

    path('company/<slug>/', EmpresaDetailView.as_view(), name="company-detail"),

    path('createCompany/', CreateCompanyView.as_view(), name="create-Company"),

    path('company/<slug>/update/', CompanyUpdateView.as_view(), name="company-update"),

    path('service/<slug>/update/', ServiceUpdateView.as_view(), name="service-update"),

    path('service/delete/<slug>', ServiceDeleteView.as_view(), name="service-delete"),

    path('service/<int:pk>/likeCompany/', ILikeCompany.as_view(), name='i-like'),
    path('service/<int:pk>/notLikedCompany/', NotLikeCompany.as_view(), name='not_like'),

    path('service/<slug>/', ServiceDetailView.as_view(), name="service-detail"),

    path('search/', ServiceSearch.as_view(), name="service-search"),




    
]