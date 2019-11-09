import django_filters
from radar.models import BaseRadares

def filter_enquadramento(queryset, name, value):
	if not value:
		return queryset

	enquadramento = value
	_enquadramento = '-'+enquadramento
	enquadramento_ = enquadramento+'-'
	if enquadramento is not None:
		_queryset = queryset.filter(enquadrame__contains=_enquadramento)
		queryset_ = queryset.filter(enquadrame__contains=enquadramento_)
		queryset = (queryset_ | _queryset).distinct()
	return queryset

class RadarFilter(django_filters.rest_framework.FilterSet):
	enquadrame = django_filters.CharFilter(method=filter_enquadramento)
	# lote = django_filters.NumberFilter()
	# tipo_equip = django_filters.CharFilter()
	# qtde_fxs_f = django_filters.NumberFilter()
	# velocidade = django_filters.CharFilter()
	# ligado = django_filters.NumberFilter()

	class Meta:
		model = BaseRadares
		fields = '__all__'