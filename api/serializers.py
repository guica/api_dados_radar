from rest_framework import serializers
from radar.models import BaseRadares, Contagens, Viagens, Trajetos
from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry


class BaseRadaresSerializer(CachedSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = [
            'id',
            'lote',
            'codigo',
            'endereco',
            'sentido',
            'referencia',
            'tipo_equip',
            'enquadrame',
            'qtde_fxs_f',
            'data_publi',
            'velocidade',
            'latitude_l',
            'latitude',
            'longitude',
            'ligado',
            'data_desli',
            'motivo_des',
            'mi_style',
            'mi_prinx',
            'geom',
            'emme_gid',
            'mdc_gid',
        ]

cache_registry.register(BaseRadaresSerializer)


class ContagensSerializer(CachedSerializerMixin, serializers.ModelSerializer):

    # acuracia = serializers.Ser

    class Meta:
        model = Contagens
        fields = [
            'data_e_hora',
            'localidade',
            'tipo',
            'contagem',
            'autuacoes',
            'placas',
            'acuracia',
            'autuacoes_por_placas'
        ]

cache_registry.register(ContagensSerializer)


class ViagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagens
        fields = [
            'id',
            'data_inicio',
            'data_final',
            'inicio',
            'final',
            'tipo',
            'distancia'
        ]


class TrajetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trajetos
        fields = '__all__'