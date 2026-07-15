from django.db import models
from django.conf import settings


class BirthDetails(models.Model):

    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="birth_details"
)

    full_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    time_of_birth = models.TimeField()

    place_of_birth = models.CharField(max_length=200)

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    timezone = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    gender = models.CharField(
    max_length=10,
    choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ],
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
    max_length=15,
    blank=True,
    )   

    notes = models.TextField(
    blank=True,
    )
    def __str__(self):
        return f"{self.full_name} ({self.user.username})"