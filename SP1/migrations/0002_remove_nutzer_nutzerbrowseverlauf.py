# Generated by Django 3.2.10 on 2022-05-17 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SP1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutzer',
            name='NutzerBrowseVerlauf',
        ),
    ]
