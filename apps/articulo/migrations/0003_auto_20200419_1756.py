# Generated by Django 3.0.5 on 2020-04-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_articulo_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='especificaciones',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='codigoArticulo',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
