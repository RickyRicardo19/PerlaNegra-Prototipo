from django.shortcuts import render
from producto.models import Producto

def inicio(request):
    template_name = 'index.html'

    contexto = {
    'producto': Producto.objects.all()
}     

    return render(request, template_name, contexto)
