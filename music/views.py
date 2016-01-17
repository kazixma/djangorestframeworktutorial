from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from music.models import Album, Track
from music.serializers import AlbumSerializer, TrackSerializer
from rest_framework.response import Response


class MusicAlbum(APIView):
    serializer_class = AlbumSerializer

    def get(self, request, id=None, format=None):
        music = Album.objects.all()
        response = self.serializer_class(music, many=True, context={'request': request})

        return Response(response.data)


class TrackList(APIView):
    serializer_class = TrackSerializer

    def get_object(self, id):
        try:
            return Track.objects.get(id=id)
        except Track.DoesNotExist:
            raise Http404

    def get(self, request, id=None, format=None):

        trackobject = self.get_object(id)
        response = self.serializer_class(trackobject)

        return Response(response.data)


musicalbum = MusicAlbum.as_view()
tracklists = TrackList.as_view()
