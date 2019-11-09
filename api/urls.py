from django.conf.urls import url
from .views import RadaresView, ContagemView, TrajetosView, ViagensView


urlpatterns = [
    url(r'^radares/', RadaresView.as_view()),
    url(r'^contagens/', ContagemView.as_view()),
    url(r'^trajetos/', TrajetosView.as_view()),
    url(r'^viagens/', ViagensView.as_view()),
]