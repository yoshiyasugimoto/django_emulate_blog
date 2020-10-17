from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect

from .models import Article, Comment


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
    if request.POST == "POST":
        Comment.objects.create(text=request.POST["text"], article=article)
    return render(request, template_name, {"article": article})


def edit_article(request, pk):
    template_name = "blogs/edit_article.html"
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404
    if request.method == "POST":
        article.title = request.POST["title"]
        article.text = request.POST["text"]
        article.save()
        return redirect(view_article, pk)
    return render(request, template_name, {"article": article})


def delete_article(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404
    article.delete()
    return redirect(article_all)


def like(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404
    article.like += 1
    article.save()
    return redirect(view_article, pk)


def api_like(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404
    article.like += 1
    article.save()

    return JsonResponse({"like": article.like})
