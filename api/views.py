# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Songs
from radar.models import BaseRadares

from .serializers import SongsSerializer, BaseRadaresSerializer
from rest_framework import generics

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

class ListRadaresView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = BaseRadares.objects.all()
    serializer_class = BaseRadaresSerializer
