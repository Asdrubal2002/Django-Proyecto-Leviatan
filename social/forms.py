from django import forms
from .models import SocialPost, SocialComment


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md w-full',
            'rows': '3',
            'placeholder': 'Escribe lo que tu quieras....'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-blue-600 hover:text-blue-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-blue-500',
        'multiple': True
        }),
        required=False
        )

    class Meta:
        model=SocialPost
        fields=['body']


class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md w-full',
            'rows': '1',
            'placeholder': 'Comenta algo....'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']


class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-blue-500 focus:border-blue-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md w-full',
            'rows': '3',
            'placeholder': '¿Que piensas?....'
            }),
        )