from django.contrib import admin

from core.models import Company, Location, Phone, Buttery


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'dt', 'location')
    search_fields = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country',)
    search_fields = ('country',)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'dt')
    search_fields = ('name',)


@admin.register(Buttery)
class ButteryAdmin(admin.ModelAdmin):
    list_display = ('volume',)
    search_fields = ('volume',)
