# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


TIPO_CHOICES = (
        (0, 'Carro'),
        (1, 'Moto'),
        (2, u'Caminhão'),
        (3,'Outro')
    )

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

    # def __unicode__(self):
    #     return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'base_radares'

class Trajetos(models.Model):

    gid         = models.AutoField(primary_key=True)
    id          = models.IntegerField(blank=True, null=True)
    viagem_id   = models.IntegerField(blank=True, null=True)
    tipo        = models.IntegerField(blank=True, null=True, choices=TIPO_CHOICES)
    data_inicio = models.DateTimeField(null=True, blank=True)
    data_final  = models.DateTimeField(null=True, blank=True)
    origem      = models.IntegerField(blank=True, null=True)
    destino     = models.IntegerField(blank=True, null=True)
    v0          = models.IntegerField(blank=True, null=True)
    v1          = models.IntegerField(blank=True, null=True)

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

    def __unicode__(self):
        return u'%s'% self.id

    class Meta:
        # managed = False
        db_table = 'contagens'