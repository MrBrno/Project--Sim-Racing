from django.shortcuts import render
from .models import race as r
from django.views.generic import DetailView

def race_views(request):
    context = {
        'races': r.objects.all()
    }
    return render(request, 'race/races.html', context)

class RaceDetailView(DetailView):
    model = r