from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


from .models import (
    Booking,
    BookingStatus,
    BookingPrice,
    BookingCheckIn,
    BookingCheckOut,
    Review,
)


class BookingList(LoginRequiredMixin, ListView):
    paginate_by = 20
    context_object_name = "booking_list"
    template_name = "bookings/booking_list.html"

    def get_queryset(self):
        current_user = self.request.user
        return Booking.objects.filter(user=current_user.id).order_by('created_at').reverse()


booking_list = BookingList.as_view()


class PlaceDetail(LoginRequiredMixin, DetailView):
    model = Booking
    context_object_name = "bookings_detail"
    template_name = "bookings/booking_detail.html"


booking_detail = PlaceDetail.as_view()
