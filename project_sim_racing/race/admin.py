from django.contrib import admin
from .models import car,track,race,car_for_the_race

admin.site.register(car)
admin.site.register(track)
admin.site.register(race)
admin.site.register(car_for_the_race)