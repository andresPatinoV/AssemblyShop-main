from django.db import models
from apps.usuario.models import Usuario

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null = False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
        

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100, blank=False, null=False)
    descripcion = models.TextField('Descripcion', blank=True, null=True)
    precio = models.FloatField('Precio', blank=False, null=False)
    cantidad = models.SmallIntegerField('Cantidad', default=1, null=False, blank=False)
    imagen = models.ImageField('Imagen', upload_to='productos/', max_length=255, blank=True, null=True)
    fecha_creacion = models.DateField('Fecha Creacion', auto_now_add=True, auto_now =False, blank=False, null=False)
    fecha_actualizacion = models.DateField('Fecha Actualizacion', auto_now_add=False, auto_now =True, blank=False, null=False)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre

    def get_precio(self):
        return self.precio

class Pc(models.Model):
    id = models.AutoField(primary_key=True)
    productos = models.ManyToManyField(Producto)
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio = models.FloatField('Precio',default=0, blank=False, null=False)
    fecha_pedido = models.DateField('Fecha Pedido', auto_now_add=True, auto_now =False, blank=True, null=True)

    class Meta:
        verbose_name = 'PC'
        verbose_name_plural = 'PCs'
    
    def __str__(self):
        return str(self.id)
