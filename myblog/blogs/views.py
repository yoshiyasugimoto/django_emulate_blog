from django.http import Http404
from django.shortcuts import render

from .models import Article


def index(request):
    template_name = "blogs/index.html"
    return render(request, template_name)


def new(request):
    template_name = "blogs/new.html"
    if request.method == "POST":
        Article.objects.create(title=request.POST["title"], text=request.POST["text"])
    return render(request, template_name)


def article_all(request):
    template_name = "blogs/article_all.html"
    articles = {"articles": Article.objects.all()}
    return render(request, template_name, articles)


def view_article(request, pk):
    template_name = "blogs/view_article.html"
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404
    return render(request, template_name, article)
