from django.contrib import admin
from .models import Empresa, Work, Homework, Image

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Work)
admin.site.register(Homework)
admin.site.register(Image)