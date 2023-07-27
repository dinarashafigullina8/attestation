from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods

from core.models import Phone


def index(request):
    return HttpResponse("<html><body>Начальная страница</body></html>")


@require_http_methods(['GET'])
def phones_list(request):
    phones = [phone['name'] + '\n' for phone in Phone.objects.all().values()]
    if phones:
        return render(request, 'core/templates/phones_list.html', context={'phones': phones})
    else:
        return redirect('')


def phone(self, pk):
    return HttpResponse(get_object_or_404(Phone, id=pk))
