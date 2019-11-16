# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import math


TIPO_CHOICES = (
        (0, 'Carro'),
        (1, 'Moto'),
        (2, u'Caminhão'),
        (3,'Outro')
    )

def distance(origin, destination):
    """
    input: 
        - origin (tuple)
        - destination (tuple)
    output:
        - distance (float)
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


class BaseRadares(models.Model):
    
    gid         = models.AutoField(primary_key=True)
    id          = models.IntegerField(blank=True, null=True)
    lote        = models.IntegerField(blank=True, null=True)
    codigo      = models.CharField(max_length=40, blank=True, null=True)
    endereco    = models.CharField(max_length=50, blank=True, null=True)
    sentido     = models.CharField(max_length=100, blank=True, null=True)
    referencia  = models.CharField(max_length=100, blank=True, null=True)
    tipo_equip  = models.CharField(max_length=30, blank=True, null=True)
    enquadrame  = models.CharField(max_length=20, blank=True, null=True)
    qtde_fxs_f  = models.IntegerField(blank=True, null=True)
    data_publi  = models.CharField(max_length=24, blank=True, null=True)
    velocidade  = models.CharField(max_length=15, blank=True, null=True)
    latitude_l  = models.CharField(max_length=50, blank=True, null=True)
    ligado      = models.IntegerField(blank=True, null=True)
    data_desli  = models.CharField(max_length=24, blank=True, null=True)
    motivo_des  = models.CharField(max_length=254, blank=True, null=True)
    mi_style    = models.CharField(max_length=254, blank=True, null=True)
    mi_prinx    = models.IntegerField(blank=True, null=True)
    geom        = models.TextField(blank=True, null=True)  # This field type is a guess.
    emme_gid    = models.IntegerField(blank=True, null=True)
    mdc_gid     = models.IntegerField(blank=True, null=True)

    def latitude(self):
        try:
            return float(self.latitude_l.split(' ')[0][1:])
        except Exception as x:
            print(x)
            return ''

    def longitude(self):
        try:
            return float(self.latitude_l.split(' ')[1][:-1])
        except Exception as x:
            print(x)
            return ''

    def contagem(self, hora, dia):
        pass

    def autuacoes(self, mes):
        pass

    def __unicode__(self):
        return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'base_radares'


class Trajetos(models.Model):

    gid         = models.AutoField(primary_key=True)
    id          = models.IntegerField(blank=True, null=True, )
    viagem_id   = models.IntegerField(blank=True, null=True, help_text='ID da Viagem', verbose_name='ID Viagem')
    tipo        = models.IntegerField(blank=True, null=True, choices=TIPO_CHOICES)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_final  = models.DateTimeField(null=True, blank=True)
    origem      = models.IntegerField(blank=True, null=True)
    destino     = models.IntegerField(blank=True, null=True)
    v0          = models.IntegerField(blank=True, null=True)
    v1          = models.IntegerField(blank=True, null=True)

    def distancia(self):
        pass

    def tempo(self):
        pass

    def velocidade_media(self):
        pass

    def __unicode__(self):
        return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'trajetos'


class Viagens(models.Model):

    gid         = models.AutoField(primary_key=True)
    id          = models.IntegerField(blank=True, null=True)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_final  = models.DateTimeField(null=True, blank=True)
    inicio      = models.IntegerField(blank=True, null=True)
    final       = models.IntegerField(blank=True, null=True)
    tipo        = models.IntegerField(blank=True, null=True, choices=TIPO_CHOICES)

    def distancia(self):
        try:
            ri=BaseRadares.objects.get(codigo__icontains=self.inicio)
            rf=BaseRadares.objects.get(codigo__icontains=self.final)
            return distance((ri.latitude(),ri.longitude()), (rf.latitude(),rf.longitude() ))
        except Exception as x:
            print(x)
            return ''

    def tempo(self):
        pass

    def __unicode__(self):
        return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'viagens'


class Contagens(models.Model):

    gid         = models.AutoField(primary_key=True)
    id          = models.IntegerField(blank=True, null=True)
    data_e_hora = models.DateTimeField(null=True, blank=True)
    localidade  = models.IntegerField(blank=True, null=True)
    tipo        = models.IntegerField(blank=True, null=True, choices=TIPO_CHOICES)
    contagem    = models.IntegerField(blank=True, null=True)
    autuacoes   = models.IntegerField(blank=True, null=True)
    placas      = models.IntegerField(blank=True, null=True)

    def acuracia(self):
        try:
            return round(float(self.placas)/float(self.contagem), 2)
        except Exception as x:
            print(x)
            return '-'

    def autuacoes_por_placas(self):
        try:
            return round(float(self.autuacoes)/float(self.placas), 2)
        except Exception as x:
            print(x)
            return '-'        

    def __unicode__(self):
        return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'contagens'