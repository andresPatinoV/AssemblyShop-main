from django.contrib import admin
from apps.tienda.models import Categoria, Producto, Pc

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['id', 'nombre']

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre', 'categoria']
    list_display = ['id', 'nombre', 'precio', 'cantidad', 'fecha_creacion', 'fecha_actualizacion', 'categoria_id']

class PcAdmin(admin.ModelAdmin):
    search_fields = ['id', 'comprador']
    list_display = ['id', 'comprador', 'precio', 'fecha_pedido']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Pc,PcAdmin)
