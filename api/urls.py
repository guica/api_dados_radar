from django.conf.urls import url
from .views import ListSongsView, ListRadaresView


urlpatterns = [
    url('songs/', ListSongsView.as_view(), name="songs-all"),
    url('radares/', ListRadaresView.as_view(), name="radares-all")
]