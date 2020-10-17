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
