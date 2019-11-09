# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BaseRadares,Trajetos, Viagens, Contagens

# Register your models here.

admin.site.register(BaseRadares)
admin.site.register(Trajetos)
admin.site.register(Viagens)
admin.site.register(Contagens)