from accounts.models import Profile
from django import forms

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    picture = forms.ImageField(label='Profile Picture',required=False, widget=forms.FileInput)
    banner = forms.ImageField(label='Banner Picture',required=False, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 mt-1 block w-full sm:text-sm border border-gray-300 rounded-md', 'rows':'3'}), max_length=260, required=False)
    birthday = forms.DateField(widget= forms.TextInput(attrs={'class':'shadow-sm focus:ring-blue-500 dark:bg-dark-third dark:text-dark-txt focus:border-blue-500 block w-full sm:text-sm border-gray-300 rounded-md'}), required=False)

    class Meta:
        model = Profile
        fields = ('first_name','last_name','picture','banner','location','url','bio','birthday')

