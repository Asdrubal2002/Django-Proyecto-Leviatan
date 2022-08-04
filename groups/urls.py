from django.urls import path

from .views import (
    GroupsView,
    GrouptDetailView,
)

app_name="groups"

urlpatterns = [

    path('groups/', GroupsView.as_view(), name="groups"),

    path('groups/<slug>/', GrouptDetailView.as_view(), name="group-detail"),


]