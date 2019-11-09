# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from radar.models import BaseRadares

from .serializers import BaseRadaresSerializer
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from .filters import RadarFilter


class FilterView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filter_class = RadarFilter
    queryset = BaseRadares.objects.all()
    serializer_class = BaseRadaresSerializer
