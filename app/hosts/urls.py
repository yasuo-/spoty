from django.urls import path

from . import views


app_name = "hosts"

urlpatterns = [
    path("new/", view=views.host_create, name="host_create"),
    path("places/new", view=views.place_create, name="place_create"),
    path("places/", view=views.place_list, name="place_list"),
    path("places/<int:pk>/", view=views.place_detail, name="place_detail"),
    path("place-items/", view=views.place_item_list, name="place_item_list"),
    path("place-items/<int:pk>/", view=views.place_item_detail, name="place_item_detail"),
    path("place-items/new", view=views.place_item_create, name="place_item_create"),
]
