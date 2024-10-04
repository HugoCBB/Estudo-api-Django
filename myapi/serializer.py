from rest_framework import serializers
from .models import Estudante, Curso

class EstudanteSerializer(serializers.Modelserializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']


class CursoSerializer(serializers.Modelserializer):
    class Meta:
        model = Curso
        fields = ['id','codigo','descricao','nivel']