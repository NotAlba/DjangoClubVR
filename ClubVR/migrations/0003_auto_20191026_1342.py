# Generated by Django 2.2.5 on 2019-10-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubVR', '0002_auto_20191025_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_fin',
            field=models.DateTimeField(verbose_name='Fecha de fin de la reserva'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name='Fecha de incio de la reserva'),
        ),
    ]
