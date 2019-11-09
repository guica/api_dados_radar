# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from radar.models import BaseRadares, Contagens, Trajetos, Viagens

from .serializers import BaseRadaresSerializer, ContagensSerializer, TrajetosSerializer, ViagensSerializer
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from .filters import RadarFilter, ContagensFilter, TrajetosFilter, ViagensFilter


class RadaresView(generics.ListAPIView):
    """
    Retorna Todas os radares com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = RadarFilter
    queryset = BaseRadares.objects.all()
    serializer_class = BaseRadaresSerializer


class ContagemView(generics.ListAPIView):
    """
    Retorna Todas os Contagens dos radares com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = ContagensFilter
    queryset = Contagens.objects.all()
    serializer_class = ContagensSerializer


class TrajetosView(generics.ListAPIView):
    """
    Retorna Todas os Trajetos com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = TrajetosFilter
    queryset = Trajetos.objects.all()
    serializer_class = TrajetosSerializer


class ViagensView(generics.ListAPIView):
    """
    Retorna Todas as viagens com ou sem uso de filtros
    """
    filter_backends = [DjangoFilterBackend]
    filter_class = ViagensFilter
    queryset = Viagens.objects.all()
    serializer_class = ViagensSerializer