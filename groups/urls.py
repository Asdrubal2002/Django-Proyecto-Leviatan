from django.urls import path

from .views import (
    GroupsView,
)

app_name="groups"

urlpatterns = [

    path('groups/', GroupsView.as_view(), name="groups"),


]