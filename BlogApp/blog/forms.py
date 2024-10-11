from .models import Blog, Comment
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','theme','description','image']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']