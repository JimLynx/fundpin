from django import forms
from .widgets import CustomClearableFileInput
from .models import Comment, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
