from rest_framework import serializers
from .models import Language, Para, Programmer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'para')


class ParaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Para
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')
