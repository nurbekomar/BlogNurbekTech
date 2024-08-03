from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from blog.models import *
# Create your views here.

menu = [{'title': 'Блог', 'url_name': 'blog'},
        {'title': 'Проект', 'url_name': 'project'},
        {'title': 'Біз жайлы', 'url_name': 'about'},]


def main(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
    }
    return render(request, 'blog/index.html', context=context)


def blog(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
    }
    return render(request, 'blog/blog.html', context=context)


def project(request):
    context = {
        'menu': menu,
    }
    return render(request, 'blog/project.html', context=context)


def about(request):
    context = {
        'menu': menu,
    }
    return render(request, 'blog/about.html', context=context)


def show_post(request, post_id):
    context = {
        'menu': menu,
    }
    return render(request, 'blog/show_post.html', context=context)


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
    }
    return render(request, 'blog/blog.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('Бұндай бет жоқ')
