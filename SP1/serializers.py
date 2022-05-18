from rest_framework import serializers
from SP1.models import Nutzer, Channel, Video

class NutzerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Nutzer
        fields=('NutzerName', 'NutzerEmailAdresse', 'NutzerPasswort')

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Channel
        fields=('ChannelId', 'ChannelPlatform', 'ChannelName', 'ChannelAnzahlSubs')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=('VideoId', 'VideoTitel', 'VideoKategorie', 'ViedeoBeschreibung', 'VideoUploadDatum')