from django.contrib import admin
from .models import Blog, Comment
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'date_created']
    list_editable = ['status']
    list_filter = ['status', 'date_created']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':['title']}


admin.site.register(Comment)