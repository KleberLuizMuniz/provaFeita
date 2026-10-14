from django.contrib import admin
from django.urls import path

from portal import views #ADICIONADO

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', views.cadastro),#ADICIONADO A ROTA VIEWS.CADASTRO
]
