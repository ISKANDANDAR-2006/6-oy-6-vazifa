
from django.contrib import admin
from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'year', 'price')
    search_fields = ('model_name', 'brand__name')
    list_filter = ('brand', 'year')
