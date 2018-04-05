from django.shortcuts import render

from rest_framework import viewsets
from .models import Language, Para, Programmer
from .serializers import LanguageSerializer, ParaSerializer, ProgrammerSerializer

# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParaView(viewsets.ModelViewSet):
    queryset = Para.objects.all()
    serializer_class = ParaSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
