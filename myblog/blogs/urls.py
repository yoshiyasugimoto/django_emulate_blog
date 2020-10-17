from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("article/all/", views.article_all, name="article_all"),
    re_path(r"article/(\d+)/", views.view_article, name="view_article"),
]
