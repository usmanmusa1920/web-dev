from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from blog.models import Comment
from .models import Message
from .forms import MessageForm, PasswordChange



def notification(request):
  if request.user.is_authenticated:
    messages_all = Message.objects.filter(is_read=False).order_by('-timestamp')
    comments_all = Comment.objects.filter(is_read=False).order_by('-timestamp')
    the_year = datetime.utcnow().year
    count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
    count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
    
    paginator_message = Paginator(messages_all, 5)
    page = request.GET.get('page')
    messages = paginator_message.get_page(page)
    paginator_comment = Paginator(comments_all, 5)
    page = request.GET.get('page')
    comments = paginator_comment.get_page(page)
    
    context = {
      'count_1': count_1,
      'count_2': count_2,
      'the_year':the_year,
      'messages': messages,
      'comments': comments
    }
    return render(request, 'notification.html', context)
  else:
    return False



def about(request):
  the_year = datetime.utcnow().year
  count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
  count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
  context = {
    'count_1': count_1,
    'count_2': count_2,
    'the_year':the_year,
  }
  return render(request, 'about.html', context)



def hireUs(request):
  the_year = datetime.utcnow().year
  count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
  count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
  context = {
    'count_1': count_1,
    'count_2': count_2,
    'the_year':the_year,
  }
  return render(request, 'hire_us.html', context)



def message(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"Your message has been sent")
      return redirect(reverse('contact_us'))
  else:
    form = MessageForm(request.POST)
    messages.success(request, f"Something went wrong try again!")
  return render(request, 'contact_us.html')



def contactUs(request):
  the_year = datetime.utcnow().year
  count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
  count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
  
  context = {
    'count_1': count_1,
    'count_2': count_2,
    'the_year':the_year,
  }
  return render(request, 'contact_us.html', context)



def changePassword(request):
  if request.user.is_authenticated:
    the_year = datetime.utcnow().year
    count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
    count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
    form = PasswordChange(user=request.user, data=request.POST or None)
    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, f'That sound great {request.user.first_name}, your password has been changed')
      return redirect(reverse('change_password'))
    else:
      context = {
        'count_1': count_1,
        'count_2': count_2,
        'the_year':the_year,
        'form': form
      }
      return render(request, 'change_password.html', context)
  else:
    return False



def markMessages(request):
  message_not_read = Message.objects.filter(is_read=False)
  if request.user.is_authenticated:
    for msg in message_not_read:
      msg.is_read = True
      msg.save()
    return redirect(reverse('notification'))
  return redirect('home')



def markMessage(request, message_id):
  message_not_read = Message.objects.get(id=message_id)
  if request.user.is_authenticated:
    message_not_read.is_read = True
    message_not_read.save()
    return redirect(reverse('notification'))
  return redirect('home')


def deleteMessage(request, message_id):
  message_not_read = Message.objects.get(id=message_id)
  if request.user.is_authenticated:
    message_not_read.delete()
    return redirect(reverse('notification'))
  return redirect('home')
