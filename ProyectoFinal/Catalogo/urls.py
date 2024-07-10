#from django.conf.urls import urls
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('principal', views.principal, name='principal'),
    path('inicio', views.inicio, name='inicio'),
    path('suscripcion', views.suscripcion, name='suscripcion'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('login', views.login, name='login'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('Principal/', views.principal, name='Principal'),
    path('registration/login', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', views.admin, name='admin'),
    path('borrar_cliente', views.borrar_cliente, name='borrar_cliente'),
    path('editar_cliente', views.editar_cliente, name='editar_cliente'),
    path('annadir_cliente', views.annadir_cliente, name='annadir_cliente'),
]