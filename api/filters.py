import django_filters
from radar.models import BaseRadares, Contagens, Viagens, Trajetos

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
	codigo = django_filters.CharFilter(lookup_expr='icontains')
	tipo_equip = django_filters.CharFilter(lookup_expr='icontains')
	enquadrame = django_filters.CharFilter(method=filter_enquadramento)
	velocidade = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = BaseRadares
		fields = ['lote','codigo','tipo_equip','enquadrame','qtde_fxs_f','velocidade','ligado']


class ContagensFilter(django_filters.rest_framework.FilterSet):
	ano = django_filters.NumberFilter(field_name='data_e_hora', lookup_expr='year')
	mes = django_filters.NumberFilter(field_name='data_e_hora', lookup_expr='month')
	dia = django_filters.NumberFilter(field_name='data_e_hora', lookup_expr='day')
	hora = django_filters.NumberFilter(field_name='data_e_hora', lookup_expr='hour')

	class Meta:
		model = Contagens
		fields = ['ano', 'mes', 'dia', 'hora', 'localidade', 'tipo', ]


class ViagensFilter(django_filters.rest_framework.FilterSet):
	class Meta:
		model = Viagens
		fields = ['id','tipo','inicio','final']


class TrajetosFilter(django_filters.rest_framework.FilterSet):

	ano = django_filters.NumberFilter(field_name='data_inicio', lookup_expr='year')
	mes = django_filters.NumberFilter(field_name='data_inicio', lookup_expr='month')
	dia = django_filters.NumberFilter(field_name='data_inicio', lookup_expr='day')
	hora = django_filters.NumberFilter(field_name='data_inicio', lookup_expr='hour')

	min_v0 = django_filters.NumberFilter(field_name="v0", lookup_expr='gte')
	max_v0 = django_filters.NumberFilter(field_name="v0", lookup_expr='lte')

	class Meta:
		model = Trajetos
		fields = ['viagem_id','tipo','origem','destino', 'min_v0','max_v0']