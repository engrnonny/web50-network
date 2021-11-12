
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new-post", views.new_post, name="new-post"),
    path("user/<slug>", views.user_profile, name="user-profile"),
    path("users/f/", views.following, name="following"),
    path("user/f/<slug>", views.follow_or_unfollow, name="follow-or-unfollow"),
    path("user/p/edit-post/<int:post_id>", views.edit_post, name="edit-post")
]
