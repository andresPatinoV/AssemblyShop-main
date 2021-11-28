from django.shortcuts import render
from django.db.models import Q
from apps.tienda.models import Producto, Categoria
from apps.tienda.forms import PcForm
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

def ensamblarPc(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    cpus = Producto.objects.filter(categoria_id=1)
    motherboards = Producto.objects.filter(categoria_id=2)
    rams = Producto.objects.filter(categoria_id=3)
    unidadesAlmacenamiento = Producto.objects.filter(categoria_id=4)
    tarjetasVideo = Producto.objects.filter(categoria_id=5)
    monitores = Producto.objects.filter(categoria_id=6)
    teclados = Producto.objects.filter(categoria_id=7)
    mouses = Producto.objects.filter(categoria_id=8)
    gabinetes = Producto.objects.filter(categoria_id=9)
    fuentes = Producto.objects.filter(categoria_id=10)
    if request.method == 'POST':
        form = request.POST
        print(form)
        cpu = Producto.objects.get(id=form['cpu'])
        print(cpu.precio)
        print(form['motherboard'])

    return render(request, 'tienda/ensamblar_pc.html', {
        'categorias':categorias, 
        'productos':productos, 
        'cpus':cpus, 
        'motherboards':motherboards,
        'rams':rams, 
        'unidadesAlmacenamiento':unidadesAlmacenamiento, 
        'tarjetasVideo':tarjetasVideo, 
        'monitores':monitores, 
        'teclados':teclados, 
        'mouses':mouses, 
        'gabinetes':gabinetes, 
        'fuentes':fuentes, 
    })
        