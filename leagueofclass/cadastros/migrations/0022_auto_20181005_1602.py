# Generated by Django 2.1.1 on 2018-10-05 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0021_auto_20181005_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='disciplina',
            field=models.OneToOneField(default='null', on_delete=django.db.models.deletion.CASCADE, to='cadastros.Disciplinas'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
    ]
