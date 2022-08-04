from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Group(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group")
    name = models.CharField(max_length=100)
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


    
    

   
