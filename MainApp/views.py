from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

author = {
    "Имя": "Никита",
    "Отчество": "Евгеньевич",
    "Фамилия":  "Меренков",
    "Телефон": "8(800)555-35-35",
    "Email": "Sizen321@mail.ru"
}

def home(request):
    print(f'{vars(request) = }')
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = F"""
    "Имя": <b>{author["Имя"]}</b><br>
    "Отчество": <b>{author['Отчество']}</b><br>
    "Фамилия":  <b>{author['Фамилия']}</b><br>
    "Телефон": <b>{author['Телефон']}</b><br>
    "Email": <b>{author['Email']}</b><br>
    """
    return HttpResponse(text)