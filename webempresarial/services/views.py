from django.shortcuts import render
from .models import Service #importar desde el modelo la Clase Service
# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, "services/services.html",{'services':services})