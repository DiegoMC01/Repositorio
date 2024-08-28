from django.urls import path
from . import views

urlpatterns = [

    path('<int:page_id>/<slug:page_slug>/',views.page, name ="page"), #<category_id>  -> es un parametro dinamico la cual es una cadena de caracteres / se agrega un int: para que el identificador sea un número

]