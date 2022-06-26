# Generated by Django 4.0.4 on 2022-05-11 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_main', '0004_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asosiy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('kanal_telegram_id', models.CharField(max_length=150, unique=True)),
                ('kanal_nomi', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AddField(
            model_name='give',
            name='time',
            field=models.TextField(default='Aniq emas'),
        ),
    ]
