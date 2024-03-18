from django.db.models import Q

from goods.models import Products


def q_search(query):
    # поиск через id 
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id=int(query))
    # поиск по ключевым словам 
    keywords = [word for word in query.split() if  len(word) > 2]
    # пустая переменная для поиска на сайте через слова
    q_objects = Q()

    for token in keywords:
        # token каждое полученное слово
        q_objects |= Q(description__icontains = token)
        q_objects |= Q(name__icontains = token)
    # возвращаем список полученных слов
    return Products.objects.filter(q_objects)