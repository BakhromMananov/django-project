from django import forms
# from django.contrib.auth.password_validation import validate_password

from store.models import *

class CreatePost(forms.Form):
    image=forms.ImageField(label='Image', widget=forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}), required=False)
    title=forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False )
    slug=forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False )
    content=forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), required=False)
    price=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False )
    rating=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False )
    category=forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label='Select category' )
    tags=forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), required=False)


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    