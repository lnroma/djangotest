# -*- coding: utf-8 -*-2
from django import forms

class CommentsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Имя'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Ваше сообщение',
        'rows':3
    }))