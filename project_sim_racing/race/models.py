from tkinter import CASCADE
from django.db import models
from django.utils import timezone

class track(models.Model):
    track_name = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.track_name
    

class car(models.Model):
    brand_name = models.CharField(max_length=50,default='')
    model_name = models.CharField(max_length=50,default='')
    in_game_name = models.CharField(max_length=50,default='ks_')
    def __str__(self):
        return self.brand_name + " " + self.model_name

class race(models.Model):
    race_bool = models.BooleanField(default=True)
    practice_time = models.IntegerField(default=5)
    quli_time = models.IntegerField(default=10)
    race_laps = models.IntegerField(default=5)
    port_number = models.IntegerField(default=8080)
    server_ip = models.CharField(max_length=20, default="195.211.11.141")
    name = models.CharField(max_length=50,default='')
    info = models.CharField(max_length=100,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def how_much_time_left(self):
        return self.time - timezone.now()
    def __str__(self):
        return self.name