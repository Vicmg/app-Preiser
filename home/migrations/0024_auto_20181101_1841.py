# Generated by Django 2.0.6 on 2018-11-01 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20181029_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='codigo_sena',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='numero_serie',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
