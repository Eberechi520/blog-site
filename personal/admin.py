from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'message', 'email']
    list_filter = ['date']