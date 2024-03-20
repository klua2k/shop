from django.shortcuts import render

# Create your views here.
def login(request):
    context ={
        'title': 'Магазин - Авторизация'
    }
    # Передаем рек, html шаблон и context 
    return render(request, 'users/login.html',context)

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

