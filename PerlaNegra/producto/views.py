from django.shortcuts import render
from producto.models import Producto

def admin_listado_de_producto(request):
    template_name = 'producto/listado.html'

    contexto = {
    'producto': Producto.objects.all()
}     

    return render(request, template_name, contexto)
