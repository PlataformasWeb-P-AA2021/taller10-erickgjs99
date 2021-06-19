from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

def index(request):
    """
        Listar los registros del modelo Estudiante, 
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # parroquias
    parroquias = Parroquia.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)


def barrios(request):
    barrios = Barrio_Ciudadela.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'barrios': barrios, 'numero_barrios': len(barrios)}
    return render(request, 'barrios.html', informacion_template)

def crear_Parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)

def crearBarrioParr(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = Parr_BarrioForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = Parr_BarrioForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrioParr.html', diccionario)

def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)

def editar_barrio(request, id):
    """
    """
    telefono = Barrio_Ciudadela.objects.get(pk=id)
    if request.method=='POST':
        formulario = Barrio_CiudadelaForm(request.POST, instance=telefono)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = Barrio_CiudadelaForm(instance=telefono)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)   
