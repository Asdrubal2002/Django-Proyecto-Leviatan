from django.shortcuts import render
from django.views import View

from django.core.paginator import Paginator

from django.shortcuts import render, redirect, get_object_or_404

from services.models import Empresa, Work

from services.forms import EmpresaModelForm, TrabajoModelForm

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse

from django.contrib import messages
# Create your views here.

import string
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.nombre)
        Klass = instance.__class__
        max_length = Klass._meta.get_field('slug').max_length
        slug = slug[:max_length]
        qs_exists = Klass.objects.filter(slug=slug).exists()

        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug[:max_length-5], randstr=random_string_generator(size=4))

            return unique_slug_generator(instance, new_slug=new_slug)
        return slug


class ServicesView(View):
    def get(self, request, *args, **kwargs):
        services = Work.objects.filter(active=True)

        digital_services_data = None

        if services:
            paginator = Paginator(services, 9)
            page_number = request.GET.get('page')
            digital_services_data = paginator.get_page(page_number)

        context = {
            'services': digital_services_data,
        }
        return render(request, 'services/services.html', context)


class EmpresaDetailView(LoginRequiredMixin, View):
    def get(self, request, slug, *args, **kwargs):
        company = Empresa.objects.get(slug=slug)
        services = Work.objects.filter(company=company)
        form = TrabajoModelForm()

        likes = company.likes.all()

        number_of_likes = len(likes)

        services_data = None

        if services:
            paginator = Paginator(services, 6)
            page_number = request.GET.get('page')
            services_data = paginator.get_page(page_number)

        context = {
            'company': company,
            'services': services_data,
            'number_of_likes': number_of_likes,
            'form': form
        }
        return render(request, 'services/my-company.html', context)

    def post(self, request, slug, *args, **kwargs):
        company = get_object_or_404(Empresa, slug=slug)
        services = Work.objects.filter(company=company)

        key = random_string_generator()

        if request.method == 'POST':
            form = TrabajoModelForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                company = get_object_or_404(Empresa, slug=slug)
                name = form.cleaned_data.get('name')
                presentation = form.cleaned_data.get('presentation')
                price = form.cleaned_data.get('price')
                thumbnail = form.cleaned_data.get('thumbnail')
                slug = key

                p, created = Work.objects.get_or_create(
                    company=company, name=name, presentation=presentation, price=price, thumbnail=thumbnail, slug=slug)
                p.save()
                messages.add_message(
                    self.request,
                    messages.SUCCESS,
                    'Haz creado un nuevo trabajo'
                )
                return redirect("services:company-detail", slug=company.slug)

        if services:
            paginator = Paginator(services, 6)
            page_number = request.GET.get('page')
            services_data = paginator.get_page(page_number)

            likes = company.likes.all()

            number_of_likes = len(likes)

            context = {
                'company': company,
                'services': services_data,
                'number_of_likes': number_of_likes,
                'form': form
            }
            return render(request, 'services/my-company.html', context)


class chooseView(View):
    def get(self, request, *args, **kwargs):
        try:
            company_detail = Empresa.objects.get(user=self.request.user)
        except Empresa.DoesNotExist:
            return redirect("services:create-Company")
        return redirect("services:company-detail", slug=company_detail.slug)


class CreateCompanyView(View):
    def get(self, request, *args, **kwargs):
        form = EmpresaModelForm()

        context = {
            'form': form
        }
        return render(request, 'services/createCompany.html', context)

    def post(self, request, *args, **kwargs):

        key = random_string_generator()

        form = EmpresaModelForm()

        if request.method == "POST":

            form = EmpresaModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.user = request.user
                banner = form.cleaned_data.get('banner')
                picture = form.cleaned_data.get('picture')
                nombre = form.cleaned_data.get('nombre')
                description = form.cleaned_data.get('description')
                lugar = form.cleaned_data.get('lugar')
                category = form.cleaned_data.get('category')
                schedule = form.cleaned_data.get('schedule')
                direction = form.cleaned_data.get('direction')
                number = form.cleaned_data.get('number')
                urlChat = form.cleaned_data.get('urlChat')
                slug = key

                p, created = Empresa.objects.get_or_create(user=form.user, banner=banner, picture=picture, nombre=nombre, description=description,
                                                           category=category, lugar=lugar, urlChat=urlChat, schedule=schedule, direction=direction, number=number, slug=slug)
                p.save()
                return redirect("services:company-detail", slug=slug)

        context = {
            'form': form
        }
        return render(request, 'services/createCompany.html', context)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "services/edit-company.html"
    form_class = EmpresaModelForm

    def get_queryset(self):
        return Empresa.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("services:services")
