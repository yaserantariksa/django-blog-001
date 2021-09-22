from django import forms
from django.forms import fields, widgets
from .models import Comment

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','content')
        widgets = {
            "name" : forms.TextInput(attrs={"class":"col-sm-6"}),
            "email" : forms.TextInput(attrs={"class":"col-sm-6"}),
            "content" : forms.TextInput(attrs={"class":"col-sm-6"}),
        }