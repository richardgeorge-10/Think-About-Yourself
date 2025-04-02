from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class FitnessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, blank=True)  # User's weight in kg
    calories_burned = models.IntegerField(null=True, blank=True)
    workout_minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

