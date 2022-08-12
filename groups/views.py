from pickle import FALSE
from tkinter import W
from tokenize import group
from unicodedata import category
from django.shortcuts import render
from django.views import View

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse

from django.core.paginator import Paginator

from groups.models import Group, Postulation
from groups.forms import GroupModelForm, PostulationModelForm

from django.views.generic.edit import UpdateView, DeleteView
from django.urls.base import reverse_lazy

from accounts.models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()


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

            form=GroupModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.user=request.user
                slug = form.cleaned_data.get('slug')
                name = form.cleaned_data.get('name')
                thumbnail = form.cleaned_data.get('thumbnail')
                description = form.cleaned_data.get('description')
                category = form.cleaned_data.get('category')
                lugar = form.cleaned_data.get('lugar')
                urlChat = form.cleaned_data.get('urlChat')
                numero_miembros = form.cleaned_data.get('numero_miembros')
                active = form.cleaned_data.get('active')

                p, created = Group.objects.get_or_create(user=form.user,slug=slug,name=name,thumbnail=thumbnail,description=description,category=category,lugar=lugar,urlChat=urlChat,numero_miembros=numero_miembros,active=active)
                p.save()
                return redirect("groups:group-list")


        digital_products_data = None

        if groups:
            paginator = Paginator(groups, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)
        
        context={
            'groups':digital_products_data
        }
        return render(request, 'groups/groups.html', context)


class GrouptDetailView(View):
    def get(self, request, slug,*args, **kwargs):
        group = get_object_or_404(Group, slug=slug)
        form = PostulationModelForm()
        context={
            'group':group,
            'form':form
        }
        return render(request, 'groups/detail.html', context)
    def post(self, request, slug, *args, **kwargs):

        if request.method == 'POST':
            form=PostulationModelForm(request.POST)
            print(form)
            if form.is_valid():
                form.user=request.user
                group = get_object_or_404(Group, slug=slug)
                presentation = form.cleaned_data.get('presentation')
                

                p, created = Postulation.objects.get_or_create(user=form.user,group=group,presentation=presentation)
                p.save()
                messages.add_message(
                self.request,
                messages.SUCCESS,
                'Te haz registrado a un grupo'
                )
                return redirect('groups:my-postulations')

        
        

class UserGroupsListView(View):
    def get(self, request, *args, **kwargs):
        groups = Group.objects.filter(user=self.request.user)
        context={
            'groups':groups
        }
        return render(request, 'groups/user_grouplist.html', context)


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    template_name="groups/edit.html"
    form_class=GroupModelForm

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("groups:group-list")


class MyPostulationsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        postulations = Postulation.objects.filter(user=self.request.user)

        postulations_data = None

        if postulations:
            paginator = Paginator(postulations, 3)
            page_number = request.GET.get('page')
            postulations_data = paginator.get_page(page_number)

        context={
            'postulations':postulations_data
        }
        return render(request, 'groups/my_postulations.html', context)


class PostulationsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        postulations = Postulation.objects.filter(group__user=self.request.user, accepted='Pendiente')

        postulations_data = None

        if postulations:
            paginator = Paginator(postulations, 6)
            page_number = request.GET.get('page')
            postulations_data = paginator.get_page(page_number)
        
        context={
            'postulations':postulations_data
        }

        return render(request, 'groups/postulations.html', context)


class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Group
    template_name='groups/delete.html'
    success_url = reverse_lazy("groups:group-list")
    
    def test_func(self):
        group = self.get_object()
        return self.request.user == group.user

    
class PostulationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Postulation
    template_name='groups/deletePostulation.html'
    success_url = reverse_lazy("groups:my-postulations")
    
    def test_func(self):
        postulation = self.get_object()
        return self.request.user == postulation.user


class AddMember(LoginRequiredMixin, View):
    def post(self, request, postulation_pk, pk, *args, **kwargs):
        postulation = Postulation.objects.get(pk=postulation_pk)
        group = Group.objects.get(pk=pk)
        members = group.members.all()
        number_of_members = len(members)
        if number_of_members < int(group.numero_miembros):
           postulation.accepted = 'Aceptada'
           postulation.save()
           group.members.add(postulation.user)
        else:
            messages.add_message(
            self.request,
            messages.WARNING,
            'Ya no puedes ingresar más personas, si quieres cambia la cantidad de personas'
            )

        members = group.members.all()
        number_of_members = len(members)
        if number_of_members == int(group.numero_miembros):
            group.active = False
            group.save()


        return redirect("groups:postulations")


class DeclineMember(LoginRequiredMixin, View):
    def post(self, request, postulation_pk, pk, *args, **kwargs):
        postulation = Postulation.objects.get(pk=postulation_pk)
        #group = Group.objects.get(pk=pk)
        postulation.accepted = 'Rechazada'
        postulation.save()
        return redirect("groups:postulations")


class GrouptMembersView(LoginRequiredMixin, View):
    def get(self, request, slug,*args, **kwargs):
        group = get_object_or_404(Group, slug=slug)
        members = group.members.all()

        members_data = None

        if members:
            paginator = Paginator(members, 4)
            page_number = request.GET.get('page')
            members_data = paginator.get_page(page_number)
        
        context={
            'members':members_data,
            'group':group,
        }
        return render(request, 'groups/members.html', context)
        

class RemoveeMember(LoginRequiredMixin, View):
    def post(self, request, member_pk, pk, *args, **kwargs):
        member = Profile.objects.get(pk=member_pk)
        group = Group.objects.get(pk=pk)
        group.members.remove(member.user)
        return redirect("groups:members", slug=group.slug)
        

class MyGroupsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        groups = Group.objects.filter(members=self.request.user)
        print(groups)
        context={
            'groups':groups
        }
        return render(request, 'groups/my_groups.html', context)


class LeaveGroup(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        group = Group.objects.get(pk=pk)
        user = request.user.id
        member = Profile.objects.get(pk=user)
        group.members.remove(member.user)
        return redirect("groups:my-groups")