from django.contrib import admin
from .models import Flight,Airport,Passenger
# Register your models here.
class flightadmin(admin.ModelAdmin):
    list_display=("id", "origin","destination","duration")

class passengeradmin(admin.ModelAdmin):
    filter_horizontal=("flights",)


admin.site.register(Flight,flightadmin)
admin.site.register(Airport)
admin.site.register(Passenger,passengeradmin)
