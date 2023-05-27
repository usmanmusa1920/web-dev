import os
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from account.models import Message
from .models import Post, Comment
from .forms import PostForm, PostFormUpdate, PostFormUpdateImg, CommentForm


def home(request):
  count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
  count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
  post_all = Post.objects.all().order_by('-pub_date')
  paginator = Paginator(post_all, 5)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  
  context = {
    'posts': posts,
    'count_1': count_1,
    'count_2': count_2,
  }
  return render(request, 'home.html', context)


def addPost(request):
  if request.user.is_authenticated:
    the_year = datetime.utcnow().year
    count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
    count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
    if request.method == 'POST':
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
        if form.cleaned_data['title'] == None and form.cleaned_data['summary'] == '' and form.cleaned_data['image_url'] == None and form.cleaned_data['image'] == None:
          messages.warning(request, f'Please write something for the post')
          return redirect(reverse('new_post'))
        else:
          instance = form.save(commit=False)
          instance.author = request.user
          instance.save()
          get_post_id = instance.id
          messages.success(request, f'You just add a new post')
          return redirect(reverse('post_detail', kwargs={'post_id': get_post_id}))
      messages.warning(request, f'Something went wrong')
    else:
      try:
        form = PostForm(request.POST, instance=request.user)
      except:
        pass
    context = {
      'count_1': count_1,
      'count_2': count_2,
      'the_year':the_year,
    }
    return render(request, 'new_post.html', context)
  else:
    return False



def postDetail(request, post_id):
  post = Post.objects.get(id=post_id)
  comments_all = post.comment_set.all().order_by('-timestamp')
  the_year = datetime.utcnow().year
  count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
  count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
  paginator = Paginator(comments_all, 5)
  page = request.GET.get('page')
  comments = paginator.get_page(page)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.post = post
      instance.save()
      return redirect(reverse('post_detail', kwargs={'post_id': post.id}))
  else:
    form = CommentForm(request.POST)
  context = {
    'count_1': count_1,
    'count_2': count_2,
    'the_year':the_year,
    'post': post,
    'comments': comments,
    'comments_all': comments_all
  }
  return render(request, 'detail.html', context)



def updatePostText(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user == post.author:
    count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
    count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
    the_year = datetime.utcnow().year
    if request.user == post.author:
      if request.method == 'POST':
        form = PostFormUpdate(request.POST, instance=post)
        if form.is_valid():
          if form.cleaned_data['title'] == None and form.cleaned_data['summary'] == '' and form.cleaned_data['image_url'] == None and post.image == '':
            messages.warning(request, f'Please write something for the post')
            return redirect(reverse('post_update_text', kwargs={'post_id': post_id}))
          form.save()
          messages.success(request, f'You just updated this post text')
          return redirect(reverse('post_detail', kwargs={'post_id': post_id}))
      else:
        form = PostFormUpdate(instance=post)
      context = {
        'count_1': count_1,
        'count_2': count_2,
        'the_year':the_year,
        'form': form
      }
      return render(request, 'update_post_text.html', context)
    return redirect('home')
  else:
    return False



def updatePostImg(request, post_id):
  post = Post.objects.get(id=post_id)
  post_2 = Post.objects.get(id=post_id)
  if request.user == post.author:
    count_1 = Message.objects.filter(is_read=False).order_by('-timestamp')
    count_2 = Comment.objects.filter(is_read=False).order_by('-timestamp')
    the_year = datetime.utcnow().year
    if request.user == post.author:
      if request.method == 'POST':
        form = PostFormUpdateImg(request.POST, request.FILES, instance=post)
        if form.is_valid():
          if post_2.image:
            r = post_2.image.path
            if os.path.exists(r):
              os.remove(r)
          form.save()
          messages.success(request, f'Your post image has been updated')
          return redirect(reverse('post_detail', kwargs={'post_id': post_id}))
        else:
          messages.warning(request, f'Something went wrong')
      else:
        form = PostFormUpdate(instance=post)
      context = {
        'count_1': count_1,
        'count_2': count_2,
        'the_year':the_year,
        'form': form,
        'post': post
      }
      return render(request, 'update_post_img.html', context)
    return False
  else:
    return False



def postDelete(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user == post.author:
    context = {
      'post': post,
    }
    return render(request, 'delete.html', context)
  else:
    return False



def postDeleteYes(request, post_id):
  post = Post.objects.get(id=post_id)
  if request.user == post.author:
    if post.image:
      r = post.image.path
      if os.path.exists(r):
        os.remove(r)
    post.delete()
    return redirect('home')
  return False



def markComment(request, comment_id):
  comment_not_read = Comment.objects.get(id=comment_id)
  if request.user.is_authenticated:
    comment_not_read.is_read = True
    comment_not_read.save()
    return redirect(reverse('notification'))
  return redirect('home')



def markComments(request):
  comment_not_read = Comment.objects.filter(is_read=False)
  if request.user.is_authenticated:
    for comments in comment_not_read:
      comments.is_read = True
      comments.save()
    return redirect(reverse('notification'))
  return redirect('home')
