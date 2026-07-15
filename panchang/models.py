from django.db import models

class Panchang(models.Model):

    tithi = models.CharField(max_length=100)

    nakshatra = models.CharField(max_length=100)

    yoga = models.CharField(max_length=100)

    karana = models.CharField(max_length=100)

    sunrise = models.TimeField()

    sunset = models.TimeField()

    hindu_month = models.CharField(max_length=100)

    paksha = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.tithi} - {self.nakshatra}"