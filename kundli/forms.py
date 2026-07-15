from django import forms

from .models import BirthDetails


class BirthDetailsForm(forms.ModelForm):

    class Meta:
        model = BirthDetails

        fields = [
            "full_name",
            "full_name",
            "gender",
            "phone_number",
            "date_of_birth",
            "time_of_birth",
            "place_of_birth",
            "notes",
        ]

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date"}
            ),

            "time_of_birth": forms.TimeInput(
                attrs={"type": "time"}
            ),
        }