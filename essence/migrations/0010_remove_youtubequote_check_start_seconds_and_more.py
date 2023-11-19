# Generated by Django 4.2.7 on 2023-11-19 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essence', '0009_youtubequote_check_start_seconds'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='youtubequote',
            name='check_start_seconds',
        ),
        migrations.AlterField(
            model_name='youtubequote',
            name='start_seconds',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
