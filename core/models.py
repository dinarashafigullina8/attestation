from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название компании')
    dt = models.DateField(verbose_name='Дата создания компании')
    location = models.OneToOneField('core.Location', related_name='company', on_delete=models.CASCADE,
                                    verbose_name='Головной офис')
    phone = models.ForeignKey('core.Phone', related_name='companies', on_delete=models.CASCADE,
                              verbose_name='Модель телефона')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Location(models.Model):
    country = models.CharField(max_length=255, verbose_name='Страна')

    class Meta:
        verbose_name = 'Головной офис'
        verbose_name_plural = 'Головные офисы'


class Phone(models.Model):
    name = models.CharField(max_length=255, verbose_name='Модель телефона')
    dt = models.DateField(verbose_name='Дата выхода')
    buttery = models.ManyToManyField('core.Buttery', related_name='phone', verbose_name='Заряд батареи')

    class Meta:
        verbose_name = 'Смартфоны'
        verbose_name_plural = 'Смартфоны'


class Buttery(models.Model):
    volume = models.IntegerField()

    class Meta:
        verbose_name = 'Батарея'
        verbose_name_plural = 'Батареи'
