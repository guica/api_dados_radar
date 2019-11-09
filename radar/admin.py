# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BaseRadares,Trajetos, Viagens, Contagens


@admin.register(BaseRadares)
class BaseRadaresAdmin(admin.ModelAdmin):

    search_fields = ['endereco',]

    list_per_page = 30

    list_display = [
        'id',
        'lote',
        'codigo',
        'endereco',
        'referencia',
        'tipo_equip',
        'qtde_fxs_f',
        'data_publi',
        'velocidade',
        'ligado'
    ]

    list_filter = [
        'lote',
        'tipo_equip',
        'qtde_fxs_f',
        'velocidade',
        'ligado',
    ]


@admin.register(Trajetos)
class TrajetosAdmin(admin.ModelAdmin):

    # search_fields = ['endereco',]

    list_per_page = 30

    list_display = [
        'id',
        'viagem_id',
        'tipo',
        'data_inicio',
        'data_final',
        'origem',
        'destino',
        'v0',
        'v1',
    ]

    list_filter = [
        'tipo',
    ]


@admin.register(Viagens)
class ViagensAdmin(admin.ModelAdmin):

    # search_fields = ['endereco',]

    list_per_page = 30

    list_display = [
        'id',
        'data_inicio',
        'data_final',
        'inicio',
        'final',
        'tipo',
    ]

    list_filter = [
        'tipo',
    ]


@admin.register(Contagens)
class ContagensAdmin(admin.ModelAdmin):

    # search_fields = ['endereco',]

    list_per_page = 30

    list_display = [
        'id',
        'data_e_hora',
        'localidade',
        'tipo',
        'contagem',
        'autuacoes',
        'placas',
    ]

    list_filter = [
        'tipo',
    ]