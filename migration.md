```angular2html
python manage.py makemigrations --name changed_my_model your_app_label - 
дает пользовательское название для миграции
```

```angular2html
python manage.py migrate --fake-initial
Для первоначальной миграции, которая создает одну или
несколько таблиц (операция CreateModel), Django проверяет,
что все эти таблицы уже существуют в базе данных, и 
выполняет фиктивную миграцию, если это так. Точно так же 
для начальной миграции, которая добавляет одно или 
несколько полей (операция AddField), Django проверяет, что
все соответствующие столбцы уже существуют в базе данных,
и применяет фиктивную миграцию, если это так.
Без –fake-initial начальные миграции обрабатываются так же, 
как и любые другие миграции.
```
Отмена миграции
```angular2html
python manage.py migrate core 0001 - вернет базу данных
к миграции 0001
```
Отмена всех миграций
```angular2html
python manage.py migrate core zero
```
Создание пустой миграции
```angular2html
python manage.py makemigrations --empty core
```