# Generated by Django 4.0.4 on 2022-05-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='give',
            name='channel',
            field=models.ManyToManyField(blank=True, related_name='gruxlar', to='bot_main.channel'),
        ),
        migrations.AlterField(
            model_name='give',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='odamlar', to='bot_main.users'),
        ),
    ]