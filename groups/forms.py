from unicodedata import category
from django import forms
from .models import Group

CATEGORIES = (
    ('Turismo', 'Turismo'),
    ('Deporte', 'Deporte'),
    ('Estudio', 'Estudio'),
    ('Voluntariados', 'Voluntariados'),
    ('Musicales', 'Musicales'),
    ('Automotriz', 'Automotriz'),
    ('Emprendimiento', 'Emprendimiento'),
    ('Entretenimiento', 'Entretenimiento'),
)


class GroupModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    
    lugar = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    urlChat = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    
    numero_miembros = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    slug = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-r'}), required=True)
    
    class Meta:
        model = Group
        fields = (
            'name',
            'thumbnail',
            'description',
            'category',
            'lugar',
            'urlChat',
            'numero_miembros',
            'slug',
            'active',
        )
