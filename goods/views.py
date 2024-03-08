from django.shortcuts import render

import goods
from goods.models import Products


# Create your views here. Список товаров на сайте
def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Магазин - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_id):
    product = Products.objects.get(id = product_id)

    context ={
        'product': product
    }

    return render(request, "goods/product.html", context = context)
