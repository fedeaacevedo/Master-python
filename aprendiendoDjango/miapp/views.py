from django.shortcuts import render, HttpResponse
from miapp.models import Article, Category
# Create your views here.

nombre = 'Federico Acevedo'
lenguajes= ['JavaScript', 'PHP', 'Python', 'Java']

year = 2021
hasta = range(year, 2051)

def index(request):
    return render(request, 'index.html', {
        'title':'Inicio',
        'mi_variable' : 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
        })

def hola(request):
    return render(request, 'hola_mundo.html')
def pagina(request):
    return render(request, 'pagina.html') 

def contacto(request):
    return render(request, 'contacto.html')


def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Usuario creado: <strong>{articulo.title}</strong> - {articulo.content}")    