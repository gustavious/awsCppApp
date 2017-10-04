from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainApp.models import *


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
        fields = ()

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id', 'direccionEntrega', 'fechaEntregaMax', 'esPagoEnEfectivo', 'latitudGeografica', 'longitudGeografica')