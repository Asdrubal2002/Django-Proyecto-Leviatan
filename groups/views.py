from unicodedata import category
from django.shortcuts import render
from django.views import View

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse

from django.core.paginator import Paginator

from groups.models import Group
from groups.forms import GroupModelForm


# Create your views here.

class GroupsView(View):
    def get(self, request, *args, **kwargs):
        groups = Group.objects.filter(active=True)
        form = GroupModelForm()

        digital_products_data = None

        if groups:
            paginator = Paginator(groups, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'groups':digital_products_data,
            'form':form
        }
        return render(request, 'groups/groups.html', context)

    def post(self, request, *args, **kwargs):
        groups = Group.objects.filter(active=True)

        form=GroupModelForm()
    
        if request.method == "POST":

            form=GroupModelForm(request.POST)
            if form.is_valid():
                form.user=request.user
                slug = form.cleaned_data.get('slug')
                name = form.cleaned_data.get('name')
                description = form.cleaned_data.get('description')
                category = form.cleaned_data.get('category')
                lugar = form.cleaned_data.get('lugar')
                urlChat = form.cleaned_data.get('urlChat')
                numero_miembros = form.cleaned_data.get('numero_miembros')
                active = form.cleaned_data.get('active')

                p, created = Group.objects.get_or_create(user=form.user,slug=slug,name=name,description=description,category=category,lugar=lugar,urlChat=urlChat,numero_miembros=numero_miembros,active=active)
                p.save()
                return redirect('/')




        digital_products_data = None

        if groups:
            paginator = Paginator(groups, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'groups':digital_products_data
        }
        return render(request, 'groups/groups.html', context)
