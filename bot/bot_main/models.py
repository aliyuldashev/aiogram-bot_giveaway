from django.db import models

class Channel(models.Model):
    id = models.AutoField(unique=True,primary_key =True)
    telegram_id = models.CharField(max_length=150,unique=True)
    username = models.CharField(max_length=300)
    title = models.CharField(max_length=300)


class Users(models.Model):
    id = models.AutoField(unique=True,primary_key =True)
    telegram_id = models.CharField(max_length=150, unique=True)
    username = models.CharField(max_length=300)
    name = models.CharField(max_length=300)

class Give(models.Model):
    id = models.AutoField(unique=True,primary_key =True)
    name = models.CharField(max_length=250)
    users = models.ManyToManyField('Users',related_name='odamlar',blank=True)
    channel = models.ManyToManyField('Channel',related_name='gruxlar',blank=True)
    admin = models.CharField(max_length=250)
    time = models.TextField(default='Aniq emas')
class Admins(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    telegram_id = models.CharField(max_length=150, unique=True)
class Asosiy(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    kanal_telegram_id = models.CharField(max_length=150, unique=True)
    kanal_nomi = models.CharField(max_length=150, unique=True)

