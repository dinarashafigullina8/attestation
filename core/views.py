from django.http import HttpResponse, Http404
from django.shortcuts import render

from core.models import Phone


def phones(request):
    phones = [phone['name'] + '\n' for phone in Phone.objects.all().values()]
    if phones:
        return HttpResponse(phones)
    else:
        return Http404('В базе пока нет моделей телефонов')

