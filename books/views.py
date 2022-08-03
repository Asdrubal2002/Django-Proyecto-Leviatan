from unicodedata import category
from django.shortcuts import render
from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse

from django.core.paginator import Paginator

from books.models import Book
from books.forms import BookModelForm


# Create your views here.


class BooksView(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(active=True)
        form = BookModelForm()

        digital_products_data = None

        if books:
            paginator = Paginator(books, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'books':digital_products_data,
            'form':form
        }
        return render(request, 'books/books.html', context)

    def post(self, request, *args, **kwargs):
        books = Book.objects.filter(active=True)

        form=BookModelForm()
    
        if request.method == "POST":

            form=BookModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.user=request.user
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                category = form.cleaned_data.get('category')
                medio = form.cleaned_data.get('medio')
                lugar = form.cleaned_data.get('lugar')
                fecha = form.cleaned_data.get('fecha')
                hora = form.cleaned_data.get('hora')
                thumbnail = form.cleaned_data.get('thumbnail')
                slug = form.cleaned_data.get('slug')
                content_url = form.cleaned_data.get('content_url')
                content_file = form.cleaned_data.get('content_file')
                price = form.cleaned_data.get('price')
                active = form.cleaned_data.get('active')

                p, created = Book.objects.get_or_create(user=form.user,name=name,description=description,category=category,medio=medio,lugar=lugar,fecha=fecha,hora=hora, thumbnail=thumbnail, slug=slug, content_url=content_url, content_file=content_file,price=price, active=active)
                p.save()
                return redirect('/')




        digital_products_data = None

        if books:
            paginator = Paginator(books, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'books':digital_products_data
        }
        return render(request, 'books/books.html', context)


class UserBooksListView(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.filter(user=self.request.user)
        context={
            'books':books
        }
        return render(request, 'books/user_booklist.html', context)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name="books/edit.html"
    form_class=BookModelForm

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("books:book-list")


class BooktDetailView(View):
    def get(self, request, slug,*args, **kwargs):
        book = get_object_or_404(Book, slug=slug)
        context={
            'book':book,
        }
        return render(request, 'books/detail.html', context)

