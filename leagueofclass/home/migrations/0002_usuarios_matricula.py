# Generated by Django 2.0.7 on 2018-09-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='matricula',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
