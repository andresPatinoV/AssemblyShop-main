from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('administracion/', panelAdministracion, name = 'administracion'),
    path('registrar_comprador/',RegistrarComprador.as_view(),name = 'registrar_usuario'),
    path('registrar_admin/',RegistrarAdministrador.as_view(),name = 'registrar_admin'),
    path('registrar_tecnico/',RegistrarTecnico.as_view(),name = 'registrar_tecnico'),
    path('lista_administradores/',ListaAdministradores.as_view(),name = 'lista_administradores'),
    path('lista_tecnicos/',ListaTecnicos.as_view(),name = 'lista_tecnicos'),
    path('eliminar_administrador/<int:id>/', eliminarAdministrador, name = 'eliminar_administrador'),
    path('eliminar_tecnico/<int:id>/', eliminarTecnico, name = 'eliminar_tecnico'),
    path('recuperar_contrasena/', recuperarContrasena, name = 'recuperar_contrasena'),
    path('confirmacion_contrasena/<int:error>/', ConfirmacionContrasena.as_view(), name = 'confirmacion_contrasena'),
    path('cambiar_contrasena/<str:token>/', cambiarContrasena, name = 'cambiar_contrasena'),

    path('registrar_producto/',RegistrarProducto.as_view(),name = 'registrar_producto'),
    path('actualizar_producto/<int:pk>/', ActualizarProducto.as_view(),name = 'actualizar_producto'),
    path('lista_productos/',ListaProductos.as_view(),name = 'lista_productos'),
    path('eliminar_producto/<int:id>/', eliminarProducto, name = 'eliminar_producto'),
    path('actualizar_existencia/<int:id>/', actualizarExistencia, name = 'actualizar_existencia'),
]
