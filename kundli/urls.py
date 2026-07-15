from django.urls import path

from .views import create_birth_details

urlpatterns = [

    path(
        "birth-details/",
        create_birth_details,
        name="birth_details"
    ),
]