from django.shortcuts import render
from rest_framework import viewsets
from . models import Curso,Estudante
from .serializer import CursoSerializer, EstudanteSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
