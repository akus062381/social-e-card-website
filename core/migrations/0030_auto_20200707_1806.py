# Generated by Django 3.0.7 on 2020-07-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20200707_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='background_color',
            field=models.CharField(choices=[('Lavender', 'Lavender'), ('LightSalmon', 'LightSalmon'), ('LightSkyBlue', 'LightSkyBlue'), ('PaleGreen', 'PaleGreen')], default='LightSkyBlue', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='border',
            field=models.CharField(choices=[('DashedBorder', 'DashedBorder'), ('NoBorder', 'NoBorder'), ('SolidBorder', 'SolidBorder'), ('DottedBorder', 'DottedBorder')], default='NoBorder', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Perpetua', 'Perpetua'), ('Copperplate', 'Copperplate'), ('Arial', 'Arial'), ('Cambria', 'Cambria'), ('Verdana', 'Verdana')], default='Perpetua', max_length=20),
        ),
    ]
