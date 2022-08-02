from django.urls import path

from .views import (
    BooksView,  
    UserBooksListView,
    BookUpdateView,
)

app_name="books"

urlpatterns = [

    path('books/', BooksView.as_view(), name="books"),
    path('library/', UserBooksListView.as_view(), name="book-list"),

    path('library/<slug>/update/', BookUpdateView.as_view(), name="book-update"),


]