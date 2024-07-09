from django.contrib import admin
from .models import Starters,desserts,main_course


class StarterDisplay(admin.ModelAdmin):
    list_display=('name','price')

class MCDisplay(admin.ModelAdmin):
    list_display=('name','price')

class DessertDisplay(admin.ModelAdmin):
    list_display=('name','price')

admin.site.register(Starters,StarterDisplay)
admin.site.register(main_course,MCDisplay)
admin.site.register(desserts,DessertDisplay)

