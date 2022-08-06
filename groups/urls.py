from django.urls import path

from .views import (
    GroupsView,
    GrouptDetailView,
    UserGroupsListView,
    GroupUpdateView,
    MyPostulationsListView,
    PostulationsListView,
)

app_name="groups"

urlpatterns = [


    path('groups/', GroupsView.as_view(), name="groups"),

    path('list-groups/', UserGroupsListView.as_view(), name="group-list"),

    path('groups/<slug>/update/', GroupUpdateView.as_view(), name="group-update"),

    path('groups/<slug>/', GrouptDetailView.as_view(), name="group-detail"),

    path('my-postulations/', MyPostulationsListView.as_view(), name="my-postulations"),

    path('postulations/', PostulationsListView.as_view(), name="postulations"),


]