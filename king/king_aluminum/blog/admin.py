from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
  model = Comment
  extra = 0
class PostAdmin(admin.ModelAdmin):
  search_fields = ('author', 'pub_date', 'title', 'image_url', 'image', 'last_modified', 'summary',)
  ordering = ('-last_modified',)
  list_filter = ('author', 'pub_date', 'title', 'last_modified')
  list_display = ('title', 'author', 'pub_date', 'last_modified', 'last_modified')
  fieldsets = (
      (None, {"fields": ('author','title','image_url','image','summary',),}),
      ('Date Information', {'fields':('pub_date',)}),
  )
  inlines = [CommentInline]
  
  
  
admin.site.register(Post, PostAdmin)
