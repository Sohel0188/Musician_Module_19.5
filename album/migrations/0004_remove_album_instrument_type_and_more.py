# Generated by Django 5.0.6 on 2024-06-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_album_instrument_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='instrument_type',
        ),
        migrations.AlterField(
            model_name='album',
            name='rerelease_date',
            field=models.DateField(default=''),
        ),
    ]
