from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()
  
  

class MessageAdmin(admin.ModelAdmin):
  search_fields = ('full_name', 'phone', 'email', 'timestamp', 'text_body', 'is_read',)
  ordering = ('-timestamp',)
  list_filter = ('full_name', 'phone', 'email', 'timestamp',)
  list_display = ('email', 'full_name', 'phone', 'timestamp',)
  fieldsets = (
      (None, {"fields": ('full_name', 'phone', 'email', 'text_body','is_read'),}),
      ('Date Information', {'fields':('timestamp',)}),
  )
  inlines = []
  
  
  
class UserAdminForm(UserAdmin):
  search_fields = ('username', 'email',)
  list_filter = ('first_name', 'last_name', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff')
  list_display = ('first_name', 'last_name', 'last_login', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff')
  # These are the field that will display when you want to edit user account via admin
  fieldsets = (
      (None , {"fields": ('password', 'username', 'email',)}),
      ('Permissions', {"fields": ('is_active','is_superuser', 'is_staff')}),
      ('Personal', {"fields": ('image_url', 'first_name', 'last_name')}),
      ('Account activity', {"fields": ('last_login',)}),
  )
  # These are the field that will display when you want to create new user account via admin
  add_fieldsets = (
    (None, {
      'classes':('wide',),
      'fields':('first_name', 'last_name', 'username', 'email', 'image_url', 'is_active', 'is_superuser', 'is_staff', 'password1', 'password2')
    }),
  )
  filter_horizontal = ()
  
  
  
admin.site.site_header = 'King\'s aluminum'
admin.site.site_title = 'King\'s aluminum'
admin.site.index_title = 'King\'s aluminum admin'

admin.site.unregister(Group)
admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdminForm)
