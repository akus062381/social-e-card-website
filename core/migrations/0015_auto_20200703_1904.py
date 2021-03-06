# Generated by Django 3.0.7 on 2020-07-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200703_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='background_color',
            field=models.CharField(choices=[('LightSalmon', 'LightSalmon'), ('Lavender', 'Lavender'), ('PaleGreen', 'PaleGreen'), ('LightSkyBlue', 'LightSkyBlue')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='border',
            field=models.CharField(choices=[('DashedBorder', 'DashedBorder'), ('SolidBorder', 'SolidBorder'), ('NoBorder', 'NoBorder'), ('DottedBorder', 'DottedBorder')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Verdana', 'Verdana'), ('Perpetua', 'Perpetua'), ('Copperplate', 'Copperplate'), ('Arial', 'Arial'), ('Cambria', 'Cambria')], default='', max_length=20),
        ),
    ]
