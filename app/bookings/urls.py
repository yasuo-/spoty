from django.urls import path

from . import views

app_name = "bookings"
urlpatterns = [
    path("", view=views.booking_list, name="booking_list"),
    path("<int:pk>", view=views.booking_detail, name="booking_detail"),
]
