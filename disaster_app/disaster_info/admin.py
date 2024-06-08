from django.contrib import admin
from .models import Disaster, Alert, Location

admin.site.register(Disaster)
admin.site.register(Alert)
admin.site.register(Location)

# Register your models here.
