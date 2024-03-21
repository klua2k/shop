from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm

# Create your views here.
def login(request):
    # при нажатие я возвращаю обычный GET ЗАПРОС form = UserLoginForm(), а если работает на странице то POST
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # Формируем клиента и проверяем есть ли он в БД
            user = auth.authenticate(username=username,password = password)
            if user:
                auth.login(request,user)
                # Перенаправляем на главную страницу
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context ={
        'title': 'Магазин - Авторизация',
        'form': form
    }
    # Передаем рек, html шаблон и context 
    return render(request, 'users/login.html', context)

def registration(request):
    context ={
        'title': 'Магазин - Регистрация'
    }
    return render(request, 'users/registration.html',context)

def profile(request):
    context ={
        'title': 'Магазин - Профиль'
    }
    return render(request, 'users/profile.html',context)

def logout(request):
    ...

