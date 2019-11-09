from django.conf.urls import url
from .views import FilterView


urlpatterns = [
    url(r'^radares/', FilterView.as_view()),
]