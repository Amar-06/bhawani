from django.urls import path

from .views import panchang_view

urlpatterns = [
    path(
        "<int:birth_detail_id>/",
        panchang_view,
        name="panchang"
    ),
]
