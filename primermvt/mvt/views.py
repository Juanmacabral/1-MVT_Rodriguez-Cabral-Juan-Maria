from django.http import HttpResponse
from .models import Familia
from django.template import Template, Context, loader


def familiares(request):
    familiar1 = Familia(Nombre='Alberto', Apellido='Rodriguez Cabral',
                        Parentesco='Mi Papa', Edad=68, FechaDeNacimiento='1955-10-16')
    familiar2 = Familia(Nombre='Maria Susana', Apellido='Moreno',
                        Parentesco='Mi Mama', Edad=67, FechaDeNacimiento='1956-06-22')
    familiar3 = Familia(Nombre='Juan Maria', Apellido='Rodriguez Cabral',
                        Parentesco='Yo', Edad=32, FechaDeNacimiento='1990-07-28')
    familiar4 = Familia(Nombre='Nicolas', Apellido='Rodriguez Cabral',
                        Parentesco='Mi hijo', Edad=4, FechaDeNacimiento='2018-03-12')
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiares2= {'Nombre': familiar1.Nombre, 'Apellido': familiar1.Apellido,
               'Parentesco': familiar1.Parentesco,'Edad': familiar1.Edad,
               'FechaDeNacimiento': familiar1.FechaDeNacimiento,
               'Nombre2': familiar2.Nombre, 'Apellido2': familiar2.Apellido,
               'Parentesco2': familiar2.Parentesco, 'Edad2': familiar2.Edad,
               'FechaDeNacimiento2': familiar1.FechaDeNacimiento,
               'Nombre3': familiar3.Nombre, 'Apellido3': familiar3.Apellido,
               'Parentesco3': familiar3.Parentesco, 'Edad3': familiar3.Edad,
               'FechaDeNacimiento3': familiar1.FechaDeNacimiento,
               'Nombre4': familiar4.Nombre, 'Apellido4': familiar4.Apellido,
               'Parentesco4': familiar4.Parentesco, 'Edad4': familiar4.Edad,
               'FechaDeNacimiento4': familiar1.FechaDeNacimiento}

    template = loader.get_template('template1.html')
    texto = template.render(familiares2)
    return HttpResponse(texto)



