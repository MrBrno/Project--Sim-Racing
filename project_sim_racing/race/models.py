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

class server1(models.Model):
    practice_server = models.BooleanField(default=False)
    name = models.CharField(max_length=50,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    minute = models.IntegerField()
    practice_time = models.IntegerField(default=5)
    qualify_time = models.IntegerField(default=10)
    race_laps = models.IntegerField(default=5)
    server_ip = models.CharField(max_length=20, default="195.211.11.141")
    port_number = models.IntegerField(default=8080)

    def time_left(self):
        return self.time - timezone.now()
    def __str__(self):
        return self.name

class server2(models.Model):
    practice_server = models.BooleanField(default=False)
    name = models.CharField(max_length=50,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
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

class server3(models.Model):
    practice_server = models.BooleanField(default=False)
    name = models.CharField(max_length=50,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
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

class server4(models.Model):
    practice_server = models.BooleanField(default=False)
    name = models.CharField(max_length=50,default='')
    track = models.ForeignKey(track, on_delete=models.CASCADE)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
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