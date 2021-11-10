from django.contrib import admin
from apps.tienda.models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre']

admin.site.register(Categoria,CategoriaAdmin)