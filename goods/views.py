from django.shortcuts import render

import goods


# Create your views here.
def catalog(request):
    context = {
        "title": "Магазин - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/t-shirt.jpg",
                "name": "Белая футболка",
                "description": "Базовая белая футболка.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/jeans1.jpg",
                "name": "Джинсы",
                "description": "Карго.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/shoes.jpg",
                "name": "Белые кроссовки",
                "description": "Повседневные белые кроссовки.",
                "price": 670.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
