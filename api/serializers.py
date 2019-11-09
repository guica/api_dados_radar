from rest_framework import serializers
from radar.models import BaseRadares


class BaseRadaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = '__all__'

class LocalizacaoRadarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = ['codigo', 'endereco']

class EnquadramentoRadarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = '__all__'
