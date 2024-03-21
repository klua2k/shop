
from django.contrib.auth.decorators import login_required
from cProfile import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

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
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                # Перенаправляем на главную страницу
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
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
            messages.success(request, f"{user.username}, Вы успешно создали аккаунт")
                # Перенаправляем на главную страницу
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context ={
        'title': 'Магазин - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)


    context ={
        'title': 'Магазин - Профиль',
        'form': form
    }
    return render(request, 'users/profile.html',context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username} Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

