from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = ['Негізгі бет', 'Проект', 'Блог', 'Біз жайлы']


def main(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {'posts': posts, 'menu': menu, 'title': 'Негізгі бет'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'Біз жайлы'})


def category(request, cat_slug):
    return HttpResponse(f'Page Category {cat_slug}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Бұндай бет жоқ')
