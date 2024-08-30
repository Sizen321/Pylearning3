from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item, Color
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

author = {
    "Имя": "Никита",
    "Отчество": "Евгеньевич",
    "Фамилия":  "Меренков",
    "Телефон": "8(800)555-35-35",
    "Email": "Sizen321@mail.ru"
}

# items = Item.objects.all()
# colors = Color.objects.all()

def home(request):
    context = {
        "name": "Меренков Никита Евгеньевич",
        "email": "sizen321@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "author": author
    }
    return render (request, "about.html", context)

def item(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, "item.html", context) 

def item_id(request, id_):
    try:
        items = Item.objects.all()
        colors = []
        if items.colors.exists():
            colors = items.colors.all()
    except ObjectDoesNotExist:
        HttpResponseNotFound(f"""<b>Товар с id={id_} не найден!</b><br><br>
                                <a href=http://127.0.0.1:8000/items>Вернуться на страницу товаров</a>""")
    else:
        context = {
                "items": items,
                "colors": colors,
            }   
        return render(request, "item_id.html", context)
    
    # for item in items: 
    #     if item.id == id_:
    #         context = {
    #             "item": item,
    #             "colors": colors,
    #         }   
    #         return render(request, "item_id.html", context)
    # return HttpResponseNotFound(f"""<b>Товар с id={id_} не найден!</b><br><br>
    #                             <a href=http://127.0.0.1:8000/items>Вернуться на страницу товаров</a>""")