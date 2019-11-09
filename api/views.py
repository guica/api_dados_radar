# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from radar.models import BaseRadares

from .serializers import BaseRadaresSerializer, LocalizacaoRadarSerializer, EnquadramentoRadarSerializer
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from .filters import RadarFilter


class ListRadaresView(generics.ListAPIView):
    """
        Lista todos os radares e todas as suas informacoes
    """
    queryset = BaseRadares.objects.all()
    serializer_class = BaseRadaresSerializer

class LocalizacaoRadarView(generics.ListAPIView):
    """
        Lista a localizacao dos radares
    """
    queryset = BaseRadares.objects.all()
    serializer_class = LocalizacaoRadarSerializer

class EnquadramentoRadarView(generics.ListAPIView):
    """
        Lista radares com o devido enquadramento
    """

    # queryset = BaseRadares.objects.all()
    serializer_class = EnquadramentoRadarSerializer

    def get_queryset(self):
        """
        Filtragem dos radares por tipo de enquadramento
        """
        queryset = BaseRadares.objects.all()
        enquadramento = self.kwargs['tipo_enquadramento']
        _enquadramento = '-'+enquadramento
        enquadramento_ = enquadramento+'-'
        if enquadramento is not None:
            _queryset = queryset.filter(enquadrame__contains=_enquadramento)
            queryset_ = queryset.filter(enquadrame__contains=enquadramento_)
            queryset = (queryset_ | _queryset).distinct()
        return queryset

class FilterView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filter_class = RadarFilter
    queryset = ''
    # filter_fields = ['lote', 'tipo_equip', 'qtde_fxs_f', 'velocidade', 'ligado', ]
    serializer_class = BaseRadaresSerializer
    

    # def get_queryset(self):
    #     print self.request.query_params
    #     print self.kwargs
    #     queryset = BaseRadares.objects.all()
    #     # enquadramento = self.kwargs['tipo_enquadramento']
    #     # _enquadramento = '-'+enquadramento
    #     # enquadramento_ = enquadramento+'-'
    #     # if enquadramento is not None:
    #     #     _queryset = queryset.filter(enquadrame__contains=_enquadramento)
    #     #     queryset_ = queryset.filter(enquadrame__contains=enquadramento_)
    #     #     queryset = (queryset_ | _queryset).distinct()
    #     return queryset