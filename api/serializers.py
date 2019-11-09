from rest_framework import serializers
from .models import Songs
from radar.models import BaseRadares


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")

class BaseRadaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = ('__all__')