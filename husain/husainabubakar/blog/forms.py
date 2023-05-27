from django import forms
from .models import Post, Comment
    
    
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'summary', 'image_url', 'image']
    
    
class PostFormUpdate(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'summary', 'image_url']
    
    
class PostFormUpdateImg(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['image']
    
    
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['full_name', 'email', 'text_body']
