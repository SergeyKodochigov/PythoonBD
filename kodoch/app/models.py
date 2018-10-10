from django.db import models

class Horse(models.Model):
    horse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    male = models.CharField(max_length=200)
    age = models.CharField(max_length=200)


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)

class Jockey(models.Model):
    jockey_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)

class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    time = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    game_name =  models.CharField(max_length=200)