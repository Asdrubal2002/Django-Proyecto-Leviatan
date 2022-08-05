from django.urls import path

from .views import (
    GroupsView,
    GrouptDetailView,
    UserGroupsListView,
    GroupUpdateView,
)

app_name="groups"

urlpatterns = [


    path('groups/', GroupsView.as_view(), name="groups"),

    path('list-groups/', UserGroupsListView.as_view(), name="group-list"),

    path('groups/<slug>/update/', GroupUpdateView.as_view(), name="group-update"),

    path('groups/<slug>/', GrouptDetailView.as_view(), name="group-detail"),




]