# FirstDjango_20082024

## Инструкция по развертыванию проекта
1. `python3 -m venv django_venv`

2. `source django_venv/bin/activate`

3. `pip install -r requirements.txt`

4. `python manage.py migrate`

4. `python manage.py runserver`

## Запуск `ipython` в контексте приложений `django`
```
python manage.py shell_plus --ipython
```

## Выгрузка и загрузка данных из БД
### Выгрузить данные из БД для приложения MainApp(все классы)
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
```

### Выгрузить данные из БД для приложения MainApp, только Item модель(один класс)
```
python manage.py dumpdata MainApp.item --indent 4 > ./fixtures/only_items.json
```


### Выгрузить данные из БД
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
```

### Выгрузить данные из БД
```
python manage.py loaddata ./fixtures/items.json
```

### Дополнительно
1. Полезное дополнение для шаблонов 'Django'
```
ext install batisteo.vscode-django
```

Добавить в 'settings.json'
```
"emmet.includeLanguages": {
        "django-html": "html",
    },
"files.associations": {
        "*.html": "django-html"
    }
```

