# Generated by Django 4.2.7 on 2023-11-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essence', '0006_youtubevideo_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideo',
            name='length',
            field=models.IntegerField(),
        ),
    ]
