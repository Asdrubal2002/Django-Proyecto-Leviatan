from django.db import models
from django.conf import settings
import os
from django.core.validators import FileExtensionValidator

User = settings.AUTH_USER_MODEL


def book_directory_path(instance, filename):
    banner_pic_name = 'book/books/{0}/{1}'.format(
        instance.name, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name

# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    medio = models.CharField(max_length=100)
    thumbnail = models.ImageField(blank=True, null=True, upload_to=book_directory_path)
    slug = models.SlugField(unique=True)

    lugar = models.CharField(blank=True, null=True, max_length=100)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    content_url = models.URLField(blank=True, null=True)
    # content_file = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    content_file = models.FileField(blank=True, null=True)
    active = models.BooleanField(default=False)
    # cents Cant be lower than 50 cents@!
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def price_display(self):
        return "{0:.2f}".format(self.price / 100)


class PurchasedBook(models.Model):
    email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
