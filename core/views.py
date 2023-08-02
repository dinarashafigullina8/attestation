from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView

from core.models import Phone


def index(request):
    return HttpResponse("<html><body>Начальная страница</body></html>")


def phone(self, pk):
    return HttpResponse(get_object_or_404(Phone, id=pk))


class PhoneListView(ListView):
    model = Phone
    template_name = 'core/templates/phones_list.html'
    context_object_name = 'appeal_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phones'] = Phone.objects.all()
        return context


class PhoneView(DetailView):
    model = Phone
    template_name = 'core/templates/phone_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
