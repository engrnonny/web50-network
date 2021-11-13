from django.contrib import admin

# Register your models here.

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['email']

class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_added']

class FollowerAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Follower, FollowerAdmin)