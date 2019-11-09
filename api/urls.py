from django.conf.urls import url
from .views import ListRadaresView, LocalizacaoRadarView, EnquadramentoRadarView, FilterView


urlpatterns = [
    url(r'^radares/', ListRadaresView.as_view()),
    url(r'^localizacao_radares/', LocalizacaoRadarView.as_view()),
    url(r'^enquadramento_radares/(?P<tipo_enquadramento>[0-9a-zA-Z_-]+)/$', EnquadramentoRadarView.as_view()),
    url(r'^filter$', FilterView.as_view()),
]