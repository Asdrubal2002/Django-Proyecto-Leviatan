from unicodedata import category
from django.shortcuts import render
from django.views import View

from django.shortcuts import render, redirect, get_object_or_404

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
                thumbnail = form.cleaned_data.get('thumbnail')
                slug = form.cleaned_data.get('slug')
                content_url = form.cleaned_data.get('content_url')
                content_file = form.cleaned_data.get('content_file')
                price = form.cleaned_data.get('price')
                active = form.cleaned_data.get('active')

                p, created = Book.objects.get_or_create(user=form.user,name=name,description=description,category=category, thumbnail=thumbnail, slug=slug, content_url=content_url, content_file=content_file,price=price, active=active)
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

