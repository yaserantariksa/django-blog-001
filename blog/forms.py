from django import forms
from django.db.models import query
from django.forms import fields, widgets
from .models import Category, Comment
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

class PostSearchForm(forms.Form):
    q = forms.CharField()
    c = forms.ModelChoiceField(queryset=Category.objects.all().order_by('name'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['c'].label = ''
        self.fields['c'].required = False
        self.fields['c'].label = 'Category'
        self.fields['c'].widget.attrs.update({'class' : 'form-select mb-2'})
        self.fields['q'].lable = 'Search For'
        self.fields['q'].widget.attrs.update({'class' : 'form-control dropdown-toggle menudd'})
        self.fields['q'].widget.attrs.update({'data-bs-toggle':'dropdown'})
        self.fields['q'].widget.attrs.update({'autofocus':True})