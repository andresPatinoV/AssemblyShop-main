import time
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView,ListView,UpdateView,DeleteView
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from apps.usuario.models import Usuario, TokenEmail
from apps.usuario.forms import LoginForm, UsuarioForm, AdminForm
from apps.usuario.mixins import RootMixin, SesionIniciada


# Create your views here.

def panelAdministracion(request):
    if request.user.is_root:
        administradores = Usuario.objects.filter(is_administrador=True).count()
        tecnicos = Usuario.objects.filter(is_tecnico_hardware=True).count()
        return render(request, 'usuarios/root/panel_root.html', {'administradores':administradores, 'tecnicos':tecnicos}) 
    else:
        return redirect('index')        


''''class PanelAdministracionR(TemplateView):
    if request.user.is_root:
        template_name = 'usuarios/root/panel_root.html' '''

class Index(TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name = 'index.html'

class IniciandoSesion(TemplateView):
    template_name = 'iniciando_sesion.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('iniciandoSesion')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class RegistrarComprador(SesionIniciada, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/registrar_comprador.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('index')
        else:
            return render(request,self.template_name,{'form':form})

class RegistrarAdministrador(RootMixin, CreateView):
    model = Usuario
    form_class = AdminForm
    template_name = 'usuarios/registrar_admin.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                cc = form.cleaned_data.get('cc'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
                is_administrador = True,
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('usuarios:administracion')
        else:
            return render(request,self.template_name,{'form':form})


class RegistrarTecnico(RootMixin, CreateView):
    model = Usuario
    form_class = AdminForm
    template_name = 'usuarios/registrar_tecnico.html'

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                cc = form.cleaned_data.get('cc'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
                is_tecnico_hardware = True,
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('usuarios:administracion')
        else:
            return render(request,self.template_name,{'form':form})


class ListaAdministradores(RootMixin, ListView):
    model = Usuario
    template_name = 'usuarios/root/administradores.html'
    context_object_name = 'administradores'
    queryset = Usuario.objects.filter(is_administrador=True)

class ListaTecnicos(RootMixin, ListView):
    model = Usuario
    template_name = 'usuarios/root/tecnicos.html'
    context_object_name = 'tecnicos'
    queryset = Usuario.objects.filter(is_tecnico_hardware=True)

def eliminarAdministrador(request, id):
    administrador = Usuario.objects.get(id = id)
    administrador.delete()
    return redirect('usuarios:lista_administradores')

def eliminarTecnico(request, id):
    tecnico = Usuario.objects.get(id = id)
    tecnico.delete()
    return redirect('usuarios:lista_tecnicos')

class ConfirmacionContrasena(TemplateView):
    """Clase que renderiza error en caso de no existir el correo ingresado"""
    template_name = 'usuarios/confirmacion_contrasena.html'

def enviar_email(token):
    template = get_template('usuarios/correo_recuperacion_contrasena.html')
    content = template.render({'token':token.id})

    email = EmailMultiAlternatives(
        'titlo del correo',
        'mensaje de descripcion del correo',
        settings.EMAIL_HOST_USER,
        [token.email]
    )
    email.attach_alternative(content, 'text/html')
    email.send()

def recuperarContrasena(request):
    if request.method == 'POST':
        email_ingresado = request.POST.get('email')
        if Usuario.objects.filter(email=email_ingresado):
            token = TokenEmail(
                fecha_actual = time.time(),
                fecha_limite = time.time()+300.0,
                email = email_ingresado,
            )
            token.save()
            enviar_email(token)
            return render(request, 'usuarios/confirmacion_contrasena.html', {'error':True})
        else:
            return render(request, 'usuarios/confirmacion_contrasena.html', {'error':False})
    else:
        return render(request, 'usuarios/recuperar_contrasena.html')

def cambiarContrasena(request,token):
    if request.method == 'GET':
        fecha = time.time()
        token = TokenEmail.objects.get(id=token)
        if fecha >= token.fecha_limite:
            return render(request, 'usuarios/tiempo_expirado.html')
        else:
            return render(request, 'usuarios/cambiar_contrasena.html', {'token': token})
    if request.method == 'POST':
        nueva_contrasena = request.POST.get('nueva_contrasena')
        token = TokenEmail.objects.get(id=token)
        usuario = Usuario.objects.get(email=token.email)
        usuario.set_password(nueva_contrasena)
        usuario.save()
        return redirect('index')
    
