from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL

def company_directory_path_profile(instance, filename):
    profile_picture_name = 'company/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


def company_directory_path_banner(instance, filename):
    profile_picture_name = 'company/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


def work_directory_path(instance, filename):
    banner_pic_name = 'company/works/{0}/{1}'.format(
        instance.name, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name


def homework_directory_path(instance, filename):
    return 'company/homeworks/{0}'.format(filename)



GROUPS_OPTIONS=(
    ('Turismo', 'Turismo'),
    ('Educacion', 'Educación'),
    ('Tecnologia', 'Tecnologia'),
    ('Aseo', 'Aseo'),
    ('Moda', 'Moda'),
    ('Artesania', 'Artesania'),
    ('Automotriz', 'Automotriz'),
    ('Gastronomia', 'Gastronomía'),
    ('Entretenimiento', 'Entretenimiento'),
    ('Inmobiliaria', 'Inmobiliaria'),
    ('Seguridad', 'Seguridad'),
)

VERIFICATION_OPTIONS=(
    ('unverified', 'unverified'),
    ('verified', 'verified'),
)

ESTATES=(
    ('Enviada', 'Enviada'),
    ('En_revision', 'En revisión'),
    ('Aceptada', 'Aceptada'),
    ('Rechazada', 'Rechazada'),
)


class Empresa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    nombre = models.CharField(unique=True, max_length=50)
    picture = models.ImageField(default='users/user_default_profile.png', upload_to=company_directory_path_profile)
    banner = models.ImageField(default='users/user_default_bg.jpg', upload_to=company_directory_path_banner)
    description = models.TextField(max_length=400)
    category = models.CharField(blank=True, null=True, max_length=100, choices=GROUPS_OPTIONS)
    lugar = models.CharField(blank=True, null=True, max_length=100)
    created_on =models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="customers")
    dislikes = models.ManyToManyField(User, blank=True, related_name="nocustomers")
    active = models.BooleanField(default=True)
    schedule = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    urlChat = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')

    def __str__(self):
        return self.nombre


class Work(models.Model):
    thumbnail = models.ImageField(blank=True, null=True, upload_to=work_directory_path)
    company = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    presentation = models.TextField(max_length=400)
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField(blank=True, null=True)

    def price_display(self):
        return "{0:.3f}".format(self.price / 1000)

    def __str__(self):
        return self.name


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ownerHomework")
    image = models.ManyToManyField('Image', blank=True)
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    presentation = models.TextField(max_length=400)
    created_on = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)
    answer = models.TextField(blank=True, null=True)
    accepted = models.CharField(blank=False, null=False, default='Enviada',max_length=100, choices=ESTATES)

class Image(models.Model):
    image = models.ImageField(upload_to=homework_directory_path, blank=True, null=True)


