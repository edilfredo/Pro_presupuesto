
from django.contrib import admin
from django.urls import path
from presupuestoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home_view, name='home'),
    path('', views.inicio_publico, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('crear-usuario/', views.crear_usuario_view, name='crear_usuario'),
    path('crear-presupuesto/', views.crear_presupuesto, name='crear_presupuesto'),
    path('lista-presupuestos/', views.lista_presupuestos, name='lista_presupuestos'),
  
]
