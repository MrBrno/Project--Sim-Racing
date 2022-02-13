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
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    time = models.DateTimeField()



    def how_much_time_left(self):
        return self.time - timezone.now()
    def __str__(self):
        return "Race at: " + str(self.time)