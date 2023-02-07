"""
URL configuration for SistemaPET project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import route as route
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from SistemaPET import pacientes
from SistemaPET.agendamentos.APIs.viewsets import AgendamentoViewSet
from SistemaPET.agendamentos.views import AgendamentoView
from SistemaPET.consulta.APIs.viewsets import ConsultaViewSet
from SistemaPET.inicio.views import InicioView
from SistemaPET.pacientes import views
from SistemaPET.pacientes.APIs.viewsets import PacienteViewSet
from SistemaPET.pacientes.views import PacientesView, ConsultarPacienteView, PaginaPacienteView
from SistemaPET.veterinarios.APIs.viewsets import VeterinarioViewSet
from SistemaPET.veterinarios.views import VeterinariosView

route = routers.DefaultRouter()

route.register(r'pacientes', PacienteViewSet, basename="Pacientes")
route.register(r'veterinarios', VeterinarioViewSet, basename="Veterinários")
route.register('agendamentos', AgendamentoViewSet, basename="Agendamentos")
route.register(r'consulta', ConsultaViewSet, basename="Consultas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(route.urls)),
    path('', InicioView.as_view(), name='inicio'),
    path('pacientes/adicionar/', PacientesView.as_view(), name='pacientes'),
    path('pacientes/<str:cpf>/', PaginaPacienteView.as_view(), name='paciente'),
    path('pacientes/', ConsultarPacienteView.as_view(), name='consulta_paciente'),
    path('veterinarios/', VeterinariosView.as_view(), name='veterinarios'),
    path('agendamento/adicionar/', AgendamentoView.as_view(), name='agendamento')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
