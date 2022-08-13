from django.urls import path

from .views import (
    GroupsView,
    GrouptDetailView,
    UserGroupsListView,
    GroupUpdateView,
    MyPostulationsListView,
    PostulationsListView,
    GroupDeleteView,
    PostulationDeleteView,
    AddMember,
    GrouptMembersView,
    DeclineMember,
    RemoveeMember,
    MyGroupsListView,
    LeaveGroup,
    GroupSearch,
)

app_name="groups"

urlpatterns = [


    path('groups/', GroupsView.as_view(), name="groups"),

    path('list-groups/', UserGroupsListView.as_view(), name="group-list"),

    path('groups/<slug>/update/', GroupUpdateView.as_view(), name="group-update"),

    path('groups/delete/<int:pk>', GroupDeleteView.as_view(), name="group-delete"),


    path('groups/<slug>/', GrouptDetailView.as_view(), name="group-detail"),

    path('my-postulations/', MyPostulationsListView.as_view(), name="my-postulations"),

    path('postulations/', PostulationsListView.as_view(), name="postulations"),

    path('postulations/delete/<int:pk>', PostulationDeleteView.as_view(), name="postulation-delete"),

    path('postulation/<int:postulation_pk>/group/<int:pk>/reply',AddMember.as_view(), name='add-member'),

    path('member/<int:member_pk>/group/<int:pk>/reply',RemoveeMember.as_view(), name='remove-member'),


    path('declinepostulation/<int:postulation_pk>/group/<int:pk>/reply',DeclineMember.as_view(), name='decline-member'),

    path('members/<slug>/', GrouptMembersView.as_view(), name="members"),

    path('my-groups/', MyGroupsListView.as_view(), name="my-groups"),

    path('leavegroup/delete/<int:pk>', LeaveGroup.as_view(), name="leave-group"),

    path('search/', GroupSearch.as_view(), name="group-search"),


]