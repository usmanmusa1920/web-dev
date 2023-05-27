from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Message


from django.contrib.auth import get_user_model
User = get_user_model()
    
    
class MessageForm(forms.ModelForm):
  class Meta:
    model = Message
    fields = ['full_name', 'phone', 'email', 'text_body']

class PasswordChange(PasswordChangeForm):
  class Meta:
    model = User
    