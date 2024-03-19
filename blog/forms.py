from django import forms
from .models import Comment
from blog.models import Post
from django.contrib.auth.forms import UserChangeForm


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control form-control-lg",
        'placeholder': "Add comment",
        'rows': "2",
    }))
    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Search Post",
    }))


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Title",
    }))
    body = forms.EmailField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Body",
        'rows': 25
    }))
    tags = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "A comma-separated list of tags",

    }), required=False)


class PostChangeForm(UserChangeForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "Title",
    }))
    body = forms.EmailField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'placeholder': "Body",
        'rows': 20
    }))
    tags = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "A comma-separated list of tags",

    }), required=False)
    tags = forms.EmailField(widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': "A comma-separated list of tags",

    }), required=False)
    pictures = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-label',
    }), required=False)

    class Meta:
        model = Post
        fields = ('title', 'body', 'tags', 'pictures')


