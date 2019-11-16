# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from radar.models import BaseRadares, Contagens, Trajetos, Viagens

from .serializers import BaseRadaresSerializer, ContagensSerializer, TrajetosSerializer, ViagensSerializer
from rest_framework import generics
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.authtoken.views import ObtainAuthToken

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import RadarFilter, ContagensFilter, TrajetosFilter, ViagensFilter


class AuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    pass

class RadaresView(generics.ListAPIView):
    """
    Retorna Todas os radares com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = RadarFilter
    queryset = BaseRadares.objects.all()
    serializer_class = BaseRadaresSerializer
    ordering_fields = ['lote','data_publi']
    # ordering = ['lote','data_publi']


class ContagemView(LoggingMixin, generics.ListAPIView):
    """
    Retorna Todas os Contagens dos radares com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = ContagensFilter
    queryset = Contagens.objects.all()
    serializer_class = ContagensSerializer
    # ordering_fields = [
    #     'data_e_hora',
    #     'localidade',
    #     'tipo',
    #     'contagem',
    #     'autuacoes',
    #     'placas',
    # ]


class TrajetosView(LoggingMixin, generics.ListAPIView):
    """
    Retorna Todas os Trajetos com ou sem uso de filtros
    """
    filter_backends = [OrderingFilter, DjangoFilterBackend, ]
    filter_class = TrajetosFilter
    queryset = Trajetos.objects.all()
    serializer_class = TrajetosSerializer
    ordering_fields = ['v0',]


class ViagensView(LoggingMixin, generics.ListAPIView):
    """
    Retorna Todas as viagens com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = ViagensFilter
    queryset = Viagens.objects.all()
    serializer_class = ViagensSerializer