from django.contrib import admin

# Register your models here.
from music.models import Album, Track


class AlbumAdmin(admin.ModelAdmin):
    fields = ['album_name','artist']

admin.site.register(Album,AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):
    fields = ['album','order','title','duration']

admin.site.register(Track,TrackAdmin)