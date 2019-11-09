from rest_framework import serializers
from radar.models import BaseRadares


class BaseRadaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseRadares
        fields = '__all__'
