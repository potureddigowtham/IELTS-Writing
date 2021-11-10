from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Acedamic_Writing_Task1
from .models import General_Writing_Task1
from .models import Academic_General_Writing_Task2

# Register your models here.
# admin.site.register(Writing)

@admin.register(Acedamic_Writing_Task1)
class Acd_Write_Task1_Model(admin.ModelAdmin):
    list_filter = ('Title', 'Image', 'Body', 'Description')
    list_display = ('Title', 'Image', 'Body', 'Description')


@admin.register(General_Writing_Task1)
class Gen_Write_Task1_Model(admin.ModelAdmin):
    list_filter = ('Title', 'Image', 'Body', 'Description')
    list_display = ('Title', 'Image', 'Body', 'Description')


@admin.register(Academic_General_Writing_Task2)
class Acd_Gen_Write_Task2_Model(admin.ModelAdmin):
    list_filter = ('Title', 'Image', 'Body', 'Description')
    list_display = ('Title', 'Image', 'Body', 'Description')