from rest_framework import serializers
from radar.models import BaseRadares, Contagens, Viagens, Trajetos


class BaseRadaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = '__all__'


class ContagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contagens
        fields = '__all__'


class ViagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagens
        fields = '__all__'


class TrajetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajetos
        fields = '__all__'