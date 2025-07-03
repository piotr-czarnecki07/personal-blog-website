from django import forms
from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        labels = {
            'title': '',
            'content': ''
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'My Article'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start writing your article...'})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        labels = {
            'name': '',
            'content': ''
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your nickname'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment...'})
        }