from django.contrib import admin
from .models import Post_content

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'time_create']
    list_filter = ['time_create']
    search_fields = ['id', 'time_create']
admin.site.register(Post_content, PostAdmin)
