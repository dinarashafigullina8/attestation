1. Создание объектов (метод save())
```
a = Location(country='USA', city='Cupertino')
a.save()
```
1.1 Создание объектов (метод create())
```
l = Location.objects.create(country='USA', city='Cupertino')
```
1.2 get_or_create()
```
obj, created = Company.objects.get_or_create(
    country='USA', city='Cupertino',
) 
```
1.3 update_or_create()
```
obj, created = Person.objects.update_or_create(
    country='USA', city='Cupertino',
)
```
1.4 bulk_create()
```angular2html
То же самое, что INSERT INTO в SQL
Этот метод вставляет предоставленный список объектов 
в базу данных эффективным образом (обычно только 1 запрос,
независимо от количества объектов), 
и возвращает созданные объекты в виде списка,
в том же порядке, в котором они были предоставлены:
objs = Company.objects.bulk_create([
...     Company(country='USA', city='Cupertino'),
...     Company(country='China', city='Beijing'),
... ])
Это не работает с отношениями «многие ко многим».
batch_size- контролирует, сколько объектов создается в одном запросе
ignore_conflicts(True)- говорит базе данных игнорировать 
отказ вставки любых строк, которые не соответствуют
ограничениям, таким как дублирование уникальных значений
update_conflicts(True)-  указывает базе данных обновить
update_fields, когда вставка строки не удалась 
из-за конфликтов
```
2. Сохранение изменений в объектах
```
a.country = 'United State of America'
a.save()
```
2.1 bulk_update()
```angular2html
То же самое, что UPDATE + SET в SQL
Этот метод эффективно обновляет заданные поля на 
предоставленных экземплярах модели, как правило,
с помощью одного запроса, и возвращает количество
обновленных объектов:
objs = [
...    Company.objects.create(country='USA', 
city='NewYork'),
...    Company.objects.create(country='China', 
city='Hong-Kong'),
... ]
objs[0].city = 'Cupertino'
objs[1].city = 'Beijing'
Entry.objects.bulk_update(objs, ['city'])
```
2.2 update()
```angular2html
Phone.objects.filter(
    name__contains='Iphone'
).update(buttery__volume=5000)
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
Phone.objects.filter(buttery__volume__gte=3000)
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
- count()
```angular2html
Phone.objects.count()
```
- in_bulk()
```angular2html

```
- latest(), earliest()
```angular2html
Company.objects.latest('dt')
Company.objects.earliest('dt')
```
- first(), last()
```angular2html
Phone.objects.first()
Phone.objects.last()
```
- aggregate()
```angular2html
>>> from django.db.models import Count
>>> q = Phone.objects.aggregate(Count('name'))
```
- exists()
```angular2html
Phone.objects.exists()
```
- delete()
```angular2html
b = Buttery.objects.get(pk=1)

Phone.objects.filter(buttery=b).delete()
```
- as_manager()
```angular2html
class PhoneQuerySet(models.QuerySet):
    def name(self):
        return self.filter(name__contains='Iphone')


class Phone(models.Model):
    ...
    name = PhoneQuerySet.as_manager()
```
- explain()
```
print(Phone.objects.filter(name__contains='Iphone'
).explain())
2 0 0 SCAN core_phone
```
- in
```angular2html
Phone.objects.filter(id__in=[1,3,5])
```
- startswith (istartswith)
```angular2html
Phone.objects.filter(name__startswith='Iphone')
```
- endswith (iendswith)
```angular2html
Phone.objects.filter(name__endswith='11')
```
- range
```angular2html
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2015, 3, 31)
Phone.objects.filter(dt__range=(start_date, end_date))
```
- date
```angular2html
Company.objects.filter(dt__date=datetime.date(2005, 1, 1))
(Эквивалентный фрагмент кода SQL для этого поиска не включен,
поскольку реализация соответствующего запроса варьируется в зависимости 
от разных механизмов баз данных.)
```
- year
```angular2html
Company.objects.filter(dt__year=1976)
```
- iso_year
```angular2html
Company.objects.filter(dt__iso_year=1976)
```
- month
```angular2html
Company.objects.filter(dt__month=12)
```
- day
```angular2html
Company.objects.filter(dt__day__gte=7)
```
- week
```angular2html
Company.objects.filter(dt__week=9)
```
- week_day
```
Company.objects.filter(dt__week_day=1)
```
- iso_week_day
```angular2html
Company.objects.filter(dt__iso_week_day=1)
```
- quarter
```angular2html
Company.objects.filter(dt__quarter=1)
```
- time
```angular2html
Company.objects.filter(dt__time=date.time(14,30))
```
- hour
```angular2html
Company.objects.filter(dt__hour=1)
```
- minute
```angular2html
Company.objects.filter(dt__minute=1)
```
- second 
```angular2html
Company.objects.filter(dt__second=1)
```
- isnull
```angular2html
Phone.objects.filter(buttery_isnull=True)
```
- regex (iregex)
```angular2html
Phone.objects.get(name__regex=r'\AIphone')
```
- aggregate
```angular2html
Phone.objects.count() - возвращает (словарь) количество телефонов
Phone.objects.filter(dt__year__gte=2020).aggregate(
Avg('buttery__volume')) - возвращает средний объем батареи
для телефонов, выпущенных не ранее 2020
Phone.objects.aggregate(Max('buttery__volume')) -
возвращается максимальный объем батареи у телефонов
```
- annotate
```angular2html
Разница агрегации и аннотации:
В отличие от этого aggregate() , annotate() это не 
конечный пункт. Результатом предложения annotate()
является объект QuerySet . Этот объект вполне может быть 
изменен операцией другого типа QuerySet , например filter(), 
order_by() или даже другими вызовами annotate()
Aggregation - обрабатывает все результаты запроса (queryset).
Annotation - обрабатывает значение каждого значения (item) 
в запросе (queryset) отдельно.
companies = Company.objects.annotate(
num_phones=Count('phone')) - возвращает Queryset, в 
котором для каждой компании вычислено количество 
выпущенных телефонов

buttery_3000 = Count('name', filter=
Q(buttery__volume__gte=3000))
buttery_5000 = Count('name', filter=
Q(buttery__volume__lte=5000))
phones = Phone.objects.annotate(buttery_3000=
buttery_3000).annotate(buttery_5000=buttery_5000) - 
возвращает список телефонов с подсчетом количества 
телефонов с батареей выше 5000 и ниже 3000

companies = Company.objects.annotate(num_phones=
Count('phone')).order_by('-num_phones')[:5] - 
возвращает список топ-5 компаний по количеству телефонов
```
- filter() и exclude() + aggregate
```angular2html
Phone.objects.filter(name__startswith=
"Iphone").aggregate(Avg('buttery__volume'))
```
- Фильтрация по аннотациям
```angular2html
Company.objects.annotate(num_phones=
Count('phone')).filter(num_phones__gt=1)
```
- Порядок предложений annotate() и filter()
```angular2html
Фильтрация влияет на аннотацию только при условии, 
что сначала идет фильтрация
```
- order_by() + annotate
```angular2html
Company.objects.annotate(num_phones=
Count('phone')).order_by('num_phones')
```
- valuess() + annotate
```angular2html
Phone.objects.values('name').annotate(average_buttery=
Avg('buttery__volume')) - получаем аннотированный 
результат только для каждого уникального названия компании. 
Это означает, что если у вас есть две компании с одним
и тем же название, их результаты будут объединены в один 
результат в выводе запроса; среднее значение будет 
вычислено как среднее по батарее телефонов обоих компаний.

Действует так же, как filter() + annotate
```
- Агрегирование аннотаций
```angular2html
Company.objects.annotate(num_phones=
Count('phone')).aggregate(Avg('num_phones')) - вернет 
среднее количество телефонов на компанию
```