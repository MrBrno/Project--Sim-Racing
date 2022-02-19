from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import RaceDetailView
urlpatterns = [
    path('', views.race_views, name="race"),
    path('race/<pk>/', RaceDetailView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()