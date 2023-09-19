from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse ("Probando pagina pricipal tp cac_23635")

#def loging (request, usuarios):
    #return HttpResponse (f"""<h1>Pagina de login{usuarios}</h1>""")

def loging (request):
    return HttpResponse ("Pagina de loging")

def farmacia (request):
    return HttpResponse ("Mas pruebas")



# Create your views here.
