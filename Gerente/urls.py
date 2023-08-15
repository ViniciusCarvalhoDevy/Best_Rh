from django.urls import path,include
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro_gerente),
    path('login/', views.logar_gerente, name='login_gerente'),
    path("home", views.home_gerente, name='home_gerente'),
    path('cadastro/salvar', views.salvar_gerente, name='salvar_gerente'),
]
