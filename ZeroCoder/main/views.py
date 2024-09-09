from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    data = reverse('data')
    test = reverse('test')
    return HttpResponse(f'<h1>Это мой первый проект на Django</h1><br>'
                        f'<a href="{data}">Перейти на страницу data</a><br>'
                        f'<a href="{test}">Перейти на страницу test</a>')

def data(request):
    home = reverse('')
    test = reverse('test')
    return HttpResponse(f'<h1>Это страница "data"</h1><br>'
                        f'<a href="{test}">Перейти на страницу test</a><br>'
                        f'<a href="{home}">Перейти на главную страницу</a>'
                        )

def test(request):
    home = reverse('')
    data = reverse('data')
    return HttpResponse(f'<h1>Это страница "test"</h1><br>'
                        f'<a href="{data}">Перейти на страницу data</a><br>'
                        f'<a href="{home}">Перейти на главную страницу</a>'
                        )




