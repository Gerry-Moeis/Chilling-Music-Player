from rest_framework import generics

from songs.models import *
from .serializers import *

class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SelectedSongView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer