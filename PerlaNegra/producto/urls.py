from django.urls import path
from . import views
app_name = 'producto'
urlpatterns = [
    path('admin/listado', views.admin_listado_de_producto, name = 'admin_listado_de_producto'),
]