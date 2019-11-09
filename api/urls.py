from django.conf.urls import url
from .views import ListSongsView


urlpatterns = [
    url('songs/', ListSongsView.as_view(), name="songs-all")
]