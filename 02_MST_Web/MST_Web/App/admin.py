from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','photo','location','created_at',)

admin.site.register(Post, PostAdmin)