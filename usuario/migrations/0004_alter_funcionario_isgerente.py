# Generated by Django 4.2.3 on 2024-12-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_funcionario_isgerente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='isGerente',
            field=models.BooleanField(),
        ),
    ]
