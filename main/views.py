from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories
# Create your views here.
def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',#название магазина
        'content': 'Магазин одежды',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Магазин - O нас',#название магазина
        'content': 'O нас',
        'text_on_page': "Информация o нас"
    }

    return render(request, 'main/about.html', context)