# Generated by Django 2.2.1 on 2019-11-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0005_auto_20191107_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_votes',
            field=models.IntegerField(default=1),
        ),
    ]
