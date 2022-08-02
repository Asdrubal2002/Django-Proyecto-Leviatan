from unicodedata import category
from django import forms
from .models import Book

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

ACCIONES = (
    ('Vendo', 'Vendo'),
    ('Alquilo', 'Alquilo'),
    ('Comparto', 'Comparto'),
    ('Regalo', 'Regalo'),
)


class BookModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    category = forms.ChoiceField(choices=CATEGORIES, widget=forms.Select(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    medio = forms.ChoiceField(choices=ACCIONES, widget=forms.Select(attrs={
                            'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

    slug = forms.CharField(widget=forms.TextInput(attrs={
                           'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-r'}), required=True)
    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'
            }),
        required=True
    )

    content_url = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-blue-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-blue-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}))

    class Meta:
        model = Book
        fields = (
            'name',
            'description',
            'category',
            'medio',
            'thumbnail',
            'slug',
            'content_url',
            'content_file',
            'active',
            'price'
        )

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        price = int(price)
        if price > 99:
            return price
        else:
            raise forms.ValidationError(
                "Price must be equal or higher than $1 == 100")
