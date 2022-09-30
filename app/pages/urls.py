from django.urls import path

from app.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from . import views

app_name = "pages"
urlpatterns = [
    path("", view=views.place_list, name="place_list"),
    path("<int:pk>", view=views.place_detail, name="place_detail"),
]
