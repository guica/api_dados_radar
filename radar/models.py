# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseRadares(models.Model):
    gid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    lote = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=40, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    sentido = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    tipo_equip = models.CharField(max_length=30, blank=True, null=True)
    enquadrame = models.CharField(max_length=20, blank=True, null=True)
    qtde_fxs_f = models.IntegerField(blank=True, null=True)
    data_publi = models.CharField(max_length=24, blank=True, null=True)
    velocidade = models.CharField(max_length=15, blank=True, null=True)
    latitude_l = models.CharField(max_length=50, blank=True, null=True)
    ligado = models.IntegerField(blank=True, null=True)
    data_desli = models.CharField(max_length=24, blank=True, null=True)
    motivo_des = models.CharField(max_length=254, blank=True, null=True)
    mi_style = models.CharField(max_length=254, blank=True, null=True)
    mi_prinx = models.IntegerField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    emme_gid = models.IntegerField(blank=True, null=True)
    mdc_gid = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'base_radares'