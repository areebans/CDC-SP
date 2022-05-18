from django.db import models

# Create your models here.

class Nutzer(models.Model):
    NutzerName = models.CharField(primary_key=True, max_length=50)
    NutzerEmailAdresse = models.EmailField(max_length=50)
    NutzerPasswort = models.CharField(max_length=50)
    #NutzerLikes = models.URLField(max_length=500)
    #NutzerBrowseVerlauf = models.URLField(max_length=500)

class Channel(models.Model):
    ChannelId = models.AutoField(primary_key=True)
    ChannelPlatform = models.CharField(max_length=20)
    ChannelName = models.CharField(max_length=50)
    ChannelAnzahlSubs = models.IntegerField()
    # ChanelProfilbild

class Video(models.Model):
    VideoId = models.AutoField(primary_key=True)
    VideoTitel = models.CharField(max_length=50)
    # VideoThumbnail
    VideoKategorie = models.CharField(max_length=50)
    ViedeoBeschreibung = models.CharField(max_length=500)
    VideoUploadDatum = models.DateField()