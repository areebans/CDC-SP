# Generated by Django 3.2.10 on 2022-05-16 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('ChannelId', models.AutoField(primary_key=True, serialize=False)),
                ('ChannelPlatform', models.CharField(max_length=20)),
                ('ChannelName', models.CharField(max_length=50)),
                ('ChannelAnzahlSubs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nutzer',
            fields=[
                ('NutzerName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('NutzerEmailAdresse', models.EmailField(max_length=50)),
                ('NutzerPasswort', models.CharField(max_length=50)),
                ('NutzerBrowseVerlauf', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('VideoId', models.AutoField(primary_key=True, serialize=False)),
                ('VideoTitel', models.CharField(max_length=50)),
                ('VideoKategorie', models.CharField(max_length=50)),
                ('ViedeoBeschreibung', models.CharField(max_length=500)),
                ('VideoUploadDatum', models.DateField()),
            ],
        ),
    ]
