# Generated by Django 3.0.7 on 2020-07-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200702_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='background_color',
            field=models.CharField(choices=[('Lavender', 'Lavender'), ('PaleGreen', 'PaleGreen'), ('LightSkyBlue', 'LightSkyBlue'), ('LightSalmon', 'LightSalmon')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='border',
            field=models.CharField(choices=[('SolidBorder', 'SolidBorder'), ('DottedBorder', 'DottedBorder'), ('DashedBorder', 'DashedBorder'), ('NoBorder', 'NoBorder')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('Arial', 'Arial'), ('Verdana', 'Verdana'), ('Cambria', 'Cambria'), ('Perpetua', 'Perpetua'), ('Copperplate', 'Copperplate')], default='', max_length=20),
        ),
    ]
