from django.contrib import admin
from apps.tienda.models import Categoria, Producto

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre']

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'categoria']
    list_display = ['id', 'nombre', 'precio', 'cantidad', 'fecha_creacion', 'fecha_actualizacion', 'categoria_id']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)