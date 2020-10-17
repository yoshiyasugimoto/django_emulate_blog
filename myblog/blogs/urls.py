from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("article/all/", views.article_all, name="article_all"),
    re_path(r"article/([0-9]+)/", views.view_article, name="view_article"),
    re_path(r"article/([0-9]+)/edit/", views.edit_article, name="edit_article"),
    re_path(r"article/([0-9]+)/delete/", views.delete_article, name="delete_article"),
    re_path(r"article/([0-9]+)/like/", views.like, name="like"),
    re_path(r"api/like/([0-9]+)/", views.api_like, name="api_like"),
]
