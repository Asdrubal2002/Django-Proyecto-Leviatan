from logging import PlaceHolder
from unicodedata import category
from django import forms
from .models import Empresa, Work

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


class EmpresaModelForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'¿Como se llama tu empresa?',
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','maxlength':'400','placeholder':'Escribe una breve presentación acerca del grupo y para quienes va dirigido.',
       'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    
    lugar = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Localidad en tu ciudad.','maxlength':'30',
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)

    urlChat = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'WhatsApp, Telegram, otra.', 'type':'url',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)
    
    schedule = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Lunes a viernes de 7Am a 5Pm',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)

    direction = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Dirección de tu empresa',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)

    number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'¿Cuantas personas quieres conocer?',
            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)        

    
    class Meta:
        model = Empresa
        fields = ('banner','picture','nombre','description','category','lugar','urlChat','schedule','direction','number')


class TrabajoModelForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre del trabajo',
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    
    presentation = forms.CharField(widget=forms.Textarea(attrs={'rows':'3','maxlength':'400','placeholder':'Escribe una breve presentación acerca de lo que puedes hacer.',
       'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ponle un precio',
                'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=False)

    class Meta:
        model = Work
        fields = ('nombre','presentation','price','thumbnail')



