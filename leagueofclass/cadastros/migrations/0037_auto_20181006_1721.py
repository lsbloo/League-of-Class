# Generated by Django 2.1.1 on 2018-10-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0036_frequencia_frequencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='frequencia',
            field=models.CharField(choices=[('Presente', 'Presente'), ('Faltou', 'Faltou')], max_length=1),
        ),
    ]
