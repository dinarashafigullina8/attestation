1. Создание объектов (метод save())
```
a = Location(country='USA', city='Cupertino')
a.save()
```

2. Сохранение изменений в объектах
```
a.country = 'United State of America'
a.save()
```
3. Сохранение полей ForeignKey и ManyToManyField
- ForeignKey
``` 
company = Company.objects.get(pk=1)
phone = Phone.objects.get(name='Iphone 11')
company.phone = phone
company.save()
```
- ManyToMany
``` 
volume = Buttery.objects.create(volume=5000)
phone.volume.add(volume)
```
4. Получение объектов
- Получение всех объектов
``` 
all_companies = Company.objects.all()
```
- Получение определенных объектов с помощью фильтров
``` 
Phone.objects.filter(dt__gte=(2020,01,01))
```
- Цепочки фильтров
``` 
Phone.objects.filter(dt__gte=(2020,01,01)).exclude(dt__year=2023)
```
- Отфильтрованные QuerySet являются уникальными
``` 
q1 = Phone.objects.filter(name__startswith="Iphone")
q2 = q1.exclude(dt__lte=datetime.date.today())
q3 = q1.filter(dt__lte=datetime.date.today())
```
- Получение одного объекта с помощью get()
``` 
one_phone = Phone.objects.get(pk=1)
```
- Ограничение QuerySet
```  
Phone.objects.all()[:5]
Phone.objects.all()[5:10]
Phone.objects.all()[:10:2]
Phone.objects.order_by('name')[0]
```
- Поиск по полям
``` 
Phone.objects.filter(name__exact='Iphone 11')
Phone.objects.filter(name__contains='Iphone 11')
```
- Поиск, который использует отношения
``` 
Company.objects.filter(phone__name='Iphone 11')
Company.objects.filter(phone__buttery__volume=3000)
```
- Охватывающие многозначные отношения
``` 
Company.objects.filter(phone__name='Iphone 11', phone__buttery__volume=3000) - компании, 
у которых выпускался iphone 11 с батареей 3000

Company.objects.filter(phone__name='Iphone 11').filter(phone__buttery__volume=3000) - компании, 
у которых выпускался iphone 11 и компании, у телефонов которых батарея 3000
```
- Фильтры могут ссылаться на поля модели
``` 
from django.db.models import F
Company.objects.filter(location__country=F('location__city'))
Объекты F() поддерживают побитовые операции с помощью .bitand(), .bitor(), .bitxor(), .bitrightshift() и .bitleftshift()
```
- Выражения могут ссылаться на преобразования
```
from django.db.models import Min
Phone.objects.aggregate(first_published_year=Min('dt_year'))
```
- Экранирующие знаки процента и подчеркивания в выражениях LIKE
``` 

```