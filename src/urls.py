from django.contrib import admin
from django.urls import path,include
from food import views

urlpatterns = [
    # path("",views.index),
    path('',views.index,name="index"),
    path('food/',include('food.urls',namespace='food')),
    path('admin/', admin.site.urls),
]
