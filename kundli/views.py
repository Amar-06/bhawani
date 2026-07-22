from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

from .forms import BirthDetailsForm


@login_required
def create_birth_details(request):

    if request.method == "POST":

        form = BirthDetailsForm(request.POST)

        if form.is_valid():

            birth_details = form.save(commit=False)

            birth_details.user = request.user

            geolocator = Nominatim(user_agent="bhawani")

            location = geolocator.geocode(
                birth_details.place_of_birth
            )

            if location:

                birth_details.latitude = location.latitude

                birth_details.longitude = location.longitude

                tf = TimezoneFinder()

                birth_details.timezone = tf.timezone_at(
                    lat=location.latitude,
                    lng=location.longitude
                )

            birth_details.save()

            return redirect(
                "panchang",
                birth_detail_id=birth_details.id
            )

    else:

        form = BirthDetailsForm()

    return render(
        request,
        "kundli/birth_details.html",
        {
            "form": form
        }
    )