from rest_framework import serializers
from music.models import Album, Track




class TrackSerializer(serializers.ModelSerializer):
    # album = serializers.HyperlinkedRelatedField(
    #
    #     view_name='track-detail',
    #     lookup_field='id',
    #     many=False,
    #     read_only=True,
    # )

    class Meta:
        model = Track
        fields = ('album','order', 'title', 'duration')


class AlbumSerializer(serializers.ModelSerializer):
    # tracks = serializers.HyperlinkedRelatedField(
    #
    #     view_name='track-detail',
    #     lookup_field='id',
    #     many=True,
    #     read_only=True,
    # )
    tracks = TrackSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')
