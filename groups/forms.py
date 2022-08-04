from unicodedata import category
from django import forms
from .models import Group

CATEGORIES = (
    ('Libros electrónicos', 'Libros electrónicos'),
    ('Libros interactivos', 'Libros interactivos'),
    ('Género lírico', 'Género lírico'),
    ('Oda', 'Oda'),
    ('Himno', 'Himno'),
    ('Elegía', 'Elegía'),
    ('Égloga', 'Égloga'),
    ('Canción', 'Canción'),
    ('Sátira', 'Sátira'),
    ('Epopeya', 'Epopeya'),
    ('Poema épico', 'Poema épico'),
    ('Romance', 'Romance'),
    ('Fábula', 'Fábula'),
    ('Cuento', 'Cuento'),
    ('Leyenda', 'Leyenda'),
    ('Novela', 'Novela'),
    ('Tragedia', 'Tragedia'),
    ('Comedia', 'Comedia'),
    ('Drama', 'Drama'),
    ('Tragicomedia', 'Tragicomedia'),
    ('Melodrama', 'Melodrama'),
    ('Biografías', 'Biografías'),
    ('Libros sagrados', 'Libros sagrados'),
    ('Libros de bolsillo', 'Libros de bolsillo'),
    ('Cómics', 'Cómics'),
    ('Sagas o Trilogías', 'Sagas o Trilogías'),
    ('Libro de partituras', 'Libro de partituras'),
    ('Historia', 'Historia'),
    ('Terror', 'Terror'),
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
            'description',
            'category',
            'lugar',
            'urlChat',
            'numero_miembros',
            'slug',
            'active',
        )
