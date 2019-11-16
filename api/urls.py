from django.conf.urls import url
from .views import RadaresView, ContagemView, TrajetosView, ViagensView, AuthTokenView
from rest_framework_cache.registry import cache_registry
from rest_framework.urlpatterns import format_suffix_patterns


cache_registry.autodiscover()


urlpatterns = [
    url(r'^radares/', RadaresView.as_view()),
    url(r'^contagens/', ContagemView.as_view()),
    url(r'^trajetos/', TrajetosView.as_view()),
    url(r'^viagens/', ViagensView.as_view()),

    # url(r'^via-mais-congestionadas/', ViagensView.as_view()),    
]

urlpatterns += [
    url(r'^auth/', AuthTokenView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)