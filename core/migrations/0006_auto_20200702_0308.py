# Generated by Django 3.0.7 on 2020-07-02 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200702_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='background_color',
            field=models.CharField(choices=[('FFA07A', 'LightSalmon'), ('00BFFF', 'LightSkyBlue'), ('98FB98', 'PaleGreen'), ('E6E6FA', 'Lavender')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='border',
            field=models.CharField(choices=[('NoBorder', 'NoBorder'), ('DashedBorder', 'DashedBorder'), ('DottedBorder', 'DottedBorder'), ('SolidBorder', 'SolidBorder')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Copperplate', 'Copperplate'), ('Perpetua', 'Perpetua'), ('Arial', 'Arial'), ('Verdana', 'Verdana'), ('Cambria', 'Cambria')], default='', max_length=20),
        ),
    ]
