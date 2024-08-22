from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

author = {
    "Имя": "Никита",
    "Отчество": "Евгеньевич",
    "Фамилия":  "Меренков",
    "Телефон": "8(800)555-35-35",
    "Email": "Sizen321@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]



def home(request):
    # print(f'{vars(request) = }')
    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Меренков Н.Е.</i><br><br>
    # <a href=http://127.0.0.1:8000/items>Перейти на страницу товаров</a>
    # """
    # return HttpResponse(text)
    return render(request, "index.html")

def about(request):
    text = F"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия:  <b>{author['Фамилия']}</b><br>
    Телефон: <b>{author['Телефон']}</b><br>
    Email: <b>{author['Email']}</b><br>
    """
    return HttpResponse(text)

def item(request):
    items_ = [f"<b>Список товаров:</b><br><ol>"]
    for item in items:
        items_.append(f"<il><b>{item.get("id")}. </b><a href='http://127.0.0.1:8000/item/{item.get("id")}'>{item.get("name")}</a></il><br>")
    return HttpResponse(items_) 

def item_id(request, id_):
    for item in items:
        if item['id'] == id_:
            text = f"""
            <b>Товар:</b> {item.get("name")} <br>
            <b>Количество:</b> {item.get("quantity")} <br><br>
            <a href=http://127.0.0.1:8000/items>Вернуться на страницу товаров</a>
            """
            return HttpResponse(text)
    return HttpResponseNotFound(f"""<b>Товар с id={id_} не найден!</b><br><br>
                                <a href=http://127.0.0.1:8000/items>Вернуться на страницу товаров</a>""")