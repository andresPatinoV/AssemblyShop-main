from django.shortcuts import render
from django.db.models import Q
from apps.tienda.models import Producto, Categoria

# Create your views here.

def getCategoria(categorias, categoria):
    for c in categorias:
        if c.nombre == categoria:
            return int(c.id)

def productosPorCategoria(request, categoria):
    queryset = request.GET.get('busqueda')
    categorias = Categoria.objects.all()
    id = getCategoria(categorias, categoria)
    productos = Producto.objects.filter(categoria_id=id)
    if queryset:
        productos = Producto.objects.filter(
            Q(categoria_id=id) & (
            Q(nombre__icontains=queryset) | 
            Q(descripcion__icontains=queryset))
        ).distinct()
    return render(request, 'tienda/productos_por_categoria.html', {'productos': productos, 'categorias':categorias, 'categoria':categoria})

def detallesProducto(request,producto_id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(id=producto_id)
    productos_similares = Producto.objects.filter(categoria_id=producto.categoria_id)
    return render(request, 'tienda/detalles_producto.html', {'producto':producto, 'productos_similares': productos_similares, 'categorias':categorias})