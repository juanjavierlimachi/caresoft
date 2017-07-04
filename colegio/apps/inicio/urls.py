from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', inicio),
    url(r'^loguin/$', loguin),

    url(r'^docentes/$', docentes),
    url(r'^privado/$', privado),
    url(r'^salir/$', salir),
    url(r'^editarperfil/$',editar_perfil),
    url(r'^nuevo/$',nuevoUser.as_view(), name='nuevoUser'),
    url(r'^DatosUsuario/$', DatosUsuario, name='listaUsuarios'),
    url(r'^verificacion/$',verificacion, name='verificacion'),
    url(r'^informeReport/$', informeReport),

    url(r'^nuevoDirector/$',nuevoDirector.as_view(), name='nuevoDirector'),
    url(r'^verDitectores/$', verDitectores, name='verDitectores'),

    url(r'^nuevoAlumno/$',nuevoAlumno.as_view(), name='nuevoAlumno'),
    url(r'^verAlumno/$', verAlumno, name='verAlumno'),

    url(r'^regisrarse/$',regisrarseUser, name='regisrarse'),
    
    url(r'^perfilUser/$',perfilUser, name='perfilUser'),
    
    url(r'^bienvenida/$',bienvenida, name='bienvenida'),
    url(r'^personal/$',personal, name='personal'),
    url(r'^mensajes/$',mensajes, name='mensajes'),
    url(r'^buscar/$',buscar, name='buscar'),
]