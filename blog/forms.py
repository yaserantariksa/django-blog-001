from django import forms
from django.forms import fields, widgets
from .models import Comment
from mptt.forms import TreeNodeChoiceField

class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].label = ''
        self.fields['parent'].widget.attrs.update({'class':'d-none'})
        self.fields['parent'].required = False
    
    class Meta:
        model = Comment

        fields = ('name','parent','email','content')
        widgets = {
            "name" : forms.TextInput(attrs={"class":" form-control col-sm-6"}),
            "email" : forms.TextInput(attrs={"class":"form-control col-sm-6"}),
            "content" : forms.TextInput(attrs={"class":"form-control col-sm-6"}),
        }