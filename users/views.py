from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm

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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # чтобы не вводить второй раз пароль при регистрации
            user = form.instance
            auth.login(request, user)
                # Перенаправляем на главную страницу
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context ={
        'title': 'Магазин - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html',context)

def profile(request):
    context ={
        'title': 'Магазин - Профиль'
    }
    return render(request, 'users/profile.html',context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

