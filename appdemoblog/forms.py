from django import forms
from django.db import models
from .models import Post, Author, Category
from django.contrib.auth.models import User


class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        # fields = ('title', 'content', 'category', 'status')
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи',}),
            'img': forms.FileInput(attrs={'class': 'form-control-file p-2',}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи',}),
            'category': forms.Select(attrs={'class': 'form-control',}),
            'author': forms.Select(attrs={'class': 'form-control',}),
            'status': forms.Select(attrs={'class': 'form-control',}),
            'updated': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': ''}),
            'publication_date': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': ''}),
        }

class CreateAuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя',}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file p-2',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'О себе',}),
        }

class CreateCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание',}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']