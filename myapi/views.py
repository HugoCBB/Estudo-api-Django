from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics

from . models import Curso,Estudante,Matricula
from .serializer import CursoSerializer, EstudanteSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        query_set = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return query_set
    serializer_class = ListaMatriculasCursoSerializer



