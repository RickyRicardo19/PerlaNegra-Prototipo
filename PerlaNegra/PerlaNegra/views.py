from django.shortcuts import render

def inicio(request):
    templates_name = 'index.html'
    contexto = {
     }
    return render(request, templates_name, contexto)

def login(request):    
    return render(request,'login.html', {})