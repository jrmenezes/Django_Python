# Generated by Django 4.1.5 on 2023-01-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo01', '0002_pessoa_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Nascimento'),
        ),
    ]
