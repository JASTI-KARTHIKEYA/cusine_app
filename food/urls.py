from django.urls import path
from . import views

app_name='food'

urlpatterns=[
    path('starters/',views.starters,name='starters'),
    path('mains/',views.maincourse,name='mains'),
    path('deserts/',views.deserts,name='deserts'),

]