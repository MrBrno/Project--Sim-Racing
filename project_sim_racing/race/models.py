from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.urls import reverse

class track(models.Model):
    track_name = models.CharField(max_length=50,default='')
    track_image = models.ImageField(upload_to='track_images',blank=True)
    def __str__(self):
        return self.track_name
    
class car(models.Model):
    brand_name = models.CharField(max_length=50,default='')
    model_name = models.CharField(max_length=50,default='')
    car_image = models.ImageField(upload_to='car_images',blank=True)
    in_game_name = models.CharField(max_length=50,default='ks_')
    def __str__(self):
        return self.brand_name + " " + self.model_name

class race(models.Model):
    practice_server = models.BooleanField(default=False)
    name = models.CharField(max_length=50,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    mod_link = models.CharField(default="", blank=True, max_length=1000)
    info = models.TextField(max_length=500,default='')
    minute = models.IntegerField()
    practice_time = models.IntegerField(default=5)
    quaulify_time = models.IntegerField(default=10)
    race_laps = models.IntegerField(default=5)
    server_ip = models.CharField(max_length=20, default="195.211.11.141")
    port_number = models.IntegerField(default=8080)


    def time_left(self):
        return self.time - timezone.now()
    def __str__(self):
        return self.name
