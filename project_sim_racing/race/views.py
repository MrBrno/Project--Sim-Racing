from django.shortcuts import render
from .models import race as r
from datetime import datetime 
def race_views(request):
    context = {
        'races': r.objects.all()
    }
    return render(request, 'race/races.html', context)

    
