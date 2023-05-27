"""king_aluminum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from datetime import datetime
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from blog import views as b_views
from account import views as a_views
from django.conf import settings
from django.conf.urls.static import static


class LoginCustom(LoginView):
  def get_context_data(self, **kwargs):
        the_year = datetime.utcnow().year
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'the_year':the_year,
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context
      
      
class LogoutCustom(LoginRequiredMixin ,LogoutView):
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            'site': current_site,
            'site_name': current_site.name,
            # 'title': _('Logged out'),
            **(self.extra_context or {})
        })
        return context



urlpatterns = [
    # authentication
    path('login/', LoginCustom.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutCustom.as_view(template_name='login.html'), name='logout'),
    path('5c4f0bfe442f90f3bd9b9f3419f04d162451b7c92682f9bacf46737dea190452/', admin.site.urls),
    
    # blog
    path('', b_views.home, name='home'),
    path('new_post/', b_views.addPost, name='new_post'),
    path('post/<int:post_id>/', b_views.postDetail, name='post_detail'),
    path('post_update_text/<int:post_id>/', b_views.updatePostText, name='post_update_text'),
    path('post_update_img/<int:post_id>/', b_views.updatePostImg, name='post_update_img'),
    path('post_delete/<int:post_id>/', b_views.postDelete, name='post_delete'),
    path('post_delete_yes/<int:post_id>/', b_views.postDeleteYes, name='post_delete_yes'),
    path('mark_comment/<int:comment_id>/', b_views.markComment, name='mark_comment'),
    path('mark_comments/', b_views.markComments, name='mark_comments'),
    
    # account
    path('message/', a_views.message, name='message'),
    path('mark_messages/', a_views.markMessages, name='mark_messages'),
    path('mark_message/<int:message_id>/', a_views.markMessage, name='mark_message'),
    path('delete_message/<int:message_id>/', a_views.deleteMessage, name='delete_message'),
    path('notification/', a_views.notification, name='notification'),
    path('about/', a_views.about, name='about'),
    path('hire_us/', a_views.hireUs, name='hire_us'),
    path('contact_us/', a_views.contactUs, name='contact_us'),
    path('change_password/', a_views.changePassword, name='change_password'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
