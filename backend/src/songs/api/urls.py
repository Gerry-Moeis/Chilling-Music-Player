from django.urls import path

from .views import *

urlpatterns = [
    path('', SongListView.as_view(), name='songList'),
    path('song/<str:pk>/', SelectedSongView.as_view(), name='selectedSong')
]