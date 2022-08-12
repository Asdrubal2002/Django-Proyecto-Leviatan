from logging import PlaceHolder
from unicodedata import category
from django import forms
from .models import Group, Postulation

CATEGORIES = (
    ('Turismo', 'Turismo'),
    ('Deporte', 'Deporte'),
    ('Estudio', 'Estudio'),
    ('Voluntariados', 'Voluntariados'),
    ('Arte', 'Arte'),
    ('Cultura', 'Cultura'),
    ('Automotriz', 'Automotriz'),
    ('Emprendimiento', 'Emprendimiento'),
    ('Entretenimiento', 'Entretenimiento'),
)


class GroupModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','maxlength':'400','placeholder':'Escribe una breve presentación acerca del grupo y para quienes va dirigido.',
       'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    
    lugar = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ciudad, localidad.','maxlength':'30',
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    urlChat = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'WhatsApp, Telegram, otra.',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    
    numero_miembros = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ciudad, localidad.','type':'number',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    slug = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-r'}), required=True)
    
    class Meta:
        model = Group
        fields = ('name','thumbnail','description','category','lugar','urlChat','numero_miembros','slug','active')


class PostulationModelForm(forms.ModelForm):
    presentation = forms.CharField(widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'Escribe una breve presentación tuya, y que esperas al participar en este grupo.','maxlength':'400',
            'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )

    class Meta:
        model = Postulation
        fields = ('presentation',)


