from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Disaster(models.Model):
    DISASTER_TYPES = [
        ('flood', 'Flood'),
        ('earthquake', 'Earthquake'),
        ('fire', 'Fire'),
        # Add more as needed
    ]
    type = models.CharField(choices=DISASTER_TYPES, max_length=50)
    description = models.TextField()
    date_occurred = models.DateTimeField()

    def __str__(self):
        return f"{self.get_type_display()} on {self.date_occurred}"

class Alert(models.Model):
    disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
class EvacuationRoute(models.Model):
    name = models.CharField(max_length=100)
    start_location = models.ForeignKey(Location, related_name='start_location', on_delete=models.CASCADE)
    end_location = models.ForeignKey(Location, related_name='end_location', on_delete=models.CASCADE)
    route_details = models.TextField()

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

# Create your models here.
