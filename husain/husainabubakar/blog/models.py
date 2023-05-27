from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
  
  
  
class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  pub_date = models.DateTimeField(default=timezone.now)
  last_modified = models.DateTimeField(auto_now=True)
  title = models.CharField(max_length=300, blank=True, null=True)
  summary = models.TextField(blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to='blog_post_pic')
  image_url = models. CharField(max_length=1000000, blank=True, null=True)
  
  def __str__(self):
    return 'Post number ' + str(self.id) + ' by ' + str(self.author) + ' on ' + str(self.pub_date)
  
  
  
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=255, blank=False, null=False)
  email = models.CharField(max_length=255, blank=False, null=False)
  text_body = models.TextField(blank=False, null=False)
  timestamp = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False)
  
  def __str__(self):
    return 'Commnt by {} on {}'.format(self.email, self.timestamp)
