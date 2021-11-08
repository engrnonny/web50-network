from django.contrib import admin

# Register your models here.

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_added']

class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'date_added']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'date_added']



admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)