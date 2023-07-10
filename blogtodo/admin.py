from django.contrib import admin
from .models import BlogModel


@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority')
    search_fields = ('title',)
    list_filter = ('created',)