from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    safety_rating = models.IntegerField(default="0")
    wins = models.IntegerField(default="0")
    poles = models.IntegerField(default="0")
    podiums = models.IntegerField(default="0")
    laps_lead = models.IntegerField(default="0")
    races_started = models.IntegerField(default="0")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
