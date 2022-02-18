from django.shortcuts import render
from .models import server1 as race1
from .models import server2 as race2
from .models import server3 as race3
from datetime import datetime 
def race_views(request):
    context = {
        'race1': race1.objects.all()
    }
    return render(request, 'race/races.html', context)

    
