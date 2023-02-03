from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_view.logout_then_login, name='logout'),

    #incluidos
    path('producto/', include('producto.urls'))
]
