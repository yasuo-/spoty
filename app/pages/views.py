from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.hosts.models import Place, PlaceItem


class PlaceList(ListView):
    model = Place
    context_object_name = "place_list"
    template_name = "pages/place_list.html"


place_list = PlaceList.as_view()


class PlaceDetail(DetailView):
    model = Place
    context_object_name = "place_detail"
    template_name = "pages/place_detail.html"


place_detail = PlaceDetail.as_view()
