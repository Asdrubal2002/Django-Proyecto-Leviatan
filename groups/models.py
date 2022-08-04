from django.db import models
from django.conf import settings
import os

User = settings.AUTH_USER_MODEL

def group_directory_path(instance, filename):
    banner_pic_name = 'groups/groups/{0}/{1}'.format(
        instance.name, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name

# Create your models here.

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group")
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(blank=True, null=True, upload_to=group_directory_path)
    description = models.TextField()
    category = models.CharField(blank=True, null=True, max_length=100)
    lugar = models.CharField(blank=True, null=True, max_length=100)
    urlChat = models.URLField(blank=True, null=True)
    numero_miembros = models.CharField(blank=False, null=False, max_length=200)
    date_created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User, blank=True, related_name="members")
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


    
    

   
