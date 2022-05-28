from django.shortcuts import render
from django.http import HttpResponse
from CoderAppFlia.models import Familiar
from django.template import loader

# Create your views here.
def Familiares(self):

    Madre=Familiar(nombre="Paula",edad=50, fechaDeNacimiento="1972-04-10")
    Padre=Familiar(nombre="Gabriel",edad=55,fechaDeNacimiento="1967-05-15")
    Hijo=Familiar(nombre="Sebastian",edad=8,fechaDeNacimiento="2014-02-21")

    Madre.save()
    Padre.save()
    Hijo.save()

    documentoDeTexto = f"Madre: {Madre.nombre} <br> Edad: {Madre.edad} <br> Fecha De Nacimiento: {Madre.fechaDeNacimiento} <br><br> Padre: {Padre.nombre} <br> Edad: {Padre.edad} <br> Fecha De Nacimiento: {Padre.fechaDeNacimiento} <br><br> Hijo: {Hijo.nombre} <br> Edad: {Hijo.edad} <br> Fecha De Nacimiento: {Hijo.fechaDeNacimiento}"


    return HttpResponse(documentoDeTexto)

def Templatefamilia(self):
    madre=Familiar(nombre="Paula",edad=50, fechaDeNacimiento="1972-04-10")
    padre=Familiar(nombre="Gabriel",edad=55,fechaDeNacimiento="1967-05-15")
    hijo=Familiar(nombre="Sebastian",edad=8,fechaDeNacimiento="2014-02-21")

    documentoDeTexto1 = f"Nombre: {madre.nombre} Edad: {madre.edad} Fecha De Nacimiento: {madre.fechaDeNacimiento}"
    documentoDeTexto2 = f"Nombre: {padre.nombre} Edad: {padre.edad} Fecha De Nacimiento: {padre.fechaDeNacimiento}"
    documentoDeTexto3 = f"Nombre: {hijo.nombre} Edad: {hijo.edad} Fecha De Nacimiento: {hijo.fechaDeNacimiento}"

    diccionario = {'madre':documentoDeTexto1, 'padre':documentoDeTexto2, 'hijo':documentoDeTexto3}

    plantilla = loader.get_template('templateflia.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)