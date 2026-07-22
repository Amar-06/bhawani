from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from kundli.models import BirthDetails
from .services.panchang_engine import PanchangEngine


@login_required
def panchang_view(request, birth_detail_id):

    birth_detail = get_object_or_404(
        BirthDetails,
        id=birth_detail_id,
        user=request.user
    )

    engine = PanchangEngine(
        birth_detail.date_of_birth,
        birth_detail.time_of_birth,
        birth_detail.latitude,
        birth_detail.longitude
    )

    context = {
        "birth_detail": birth_detail,
        "nakshatra": engine.get_nakshatra(),
        "tithi": engine.get_tithi(),
        "yoga": engine.get_yoga(),
        "karana": engine.get_karana(),
    }

    return render(
        request,
        "panchang/panchang.html",
        context
    )