from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.tienda.views import *

urlpatterns = [
    path('<str:categoria>/', productosPorCategoria, name = 'productos_por_categoria'),
]