
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from Proyectoweb_app.models import Curso, Profesor, Entregable, Estudiante
from Proyectoweb_app.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario, EstudianteFormulario

# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)

def inicio(request):

      return render(request, "inicio.html")

def estudiantes(request):
      if request.method == "POST":
            miFormulario = EstudianteFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  estudiantes = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
                  estudiantes.save()
                  return render(request, "estudiantes.html")
      else:
                  miFormulario= EntregableFormulario()
      return render (request, "estudiantes.html", {"miFormulario": miFormulario})


    




def entregables(request):
      if request.method == 'POST':
            miFormulario = EntregableFormulario(request.POST)
            print(miFormulario)

            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  entregables = Entregable(nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'])
                  entregables.save()
                  return render (request, "entregables.html")
      else:
                  miFormulario= EntregableFormulario()
      return render (request, "entregables.html", {"miFormulario": miFormulario})

      


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["nombre"]:

	      
            nombre = request.GET['nombre'] 
            estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)

            return render(request, "inicio.html", {"estudiantes":estudiantes, })
      else:
            return HttpResponse("CAMPO VACIO")

