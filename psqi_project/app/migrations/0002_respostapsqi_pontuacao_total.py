# Generated by Django 5.1.1 on 2024-09-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respostapsqi',
            name='pontuacao_total',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
