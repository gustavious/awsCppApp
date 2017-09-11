from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainApp.models import Envio


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EnvioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Envio
        fields = ('fechaSolicitud', 'direccionEntrega', 'fechaEntregaMaxima', 'code')