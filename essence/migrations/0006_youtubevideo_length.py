# Generated by Django 4.2.7 on 2023-11-17 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essence', '0005_youtubequote_id_alter_textquote_metadata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='length',
            field=models.TimeField(default=datetime.time(0, 0)),
            preserve_default=False,
        ),
    ]
