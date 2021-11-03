
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('hola/', views.hola, name='hola'),
    path('pagina/', views.pagina, name='pagina'),
    path('contacto/', views.contacto, name='contacto'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name='crear_articulo'),
]
