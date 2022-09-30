from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _

from .models import Host, Place, PlaceItem
from .forms import (
    HostModelForm,
    PlaceModelForm,
    PlaceItemModelForm
)

from app.address.models import Prefecture, City, Address


class CreateHostView(CreateView):
    form_class = HostModelForm
    model = Host
    template_name = '/hosts/new.html'
    # success_url = reverse_lazy('hosts:place_create')
    success_message = _("正常に作成されました")

    def get(self, request, *args, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context.update({
            'user': self.request.user,
        })

        return render(request, '/hosts/new.html', context=context)

    def get_success_url(self):
        return reverse_lazy('hosts:place_create')


host_create = CreateHostView.as_view()


class PlaceHostView(CreateView):
    form_class = HostModelForm
    model = Host
    template_name = '/hosts/place_create.html'
    success_url = reverse_lazy('hosts:place_list')
    success_message = _("正常に作成されました")


place_create = CreateHostView.as_view()


class PlaceListView(LoginRequiredMixin, ListView):
    template_name = 'admin/place/place_list.html'
    model = Place
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()

        context.update({
            'user': self.request.user,
            'host': host,
        })

        return context


place_list = PlaceListView.as_view()


class PlaceDetailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'admin/place/place_detail.html'
    model = Place
    form_class = PlaceModelForm
    success_url = reverse_lazy('place_list')
    success_message = _("正常に更新されました")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()
        context.update({
            'user': self.request.user,
            'host': host,
        })

        return context


place_detail = PlaceDetailView.as_view()


class PlaceItemListView(LoginRequiredMixin, ListView):
    template_name = 'admin/place/place_item_list.html'
    model = PlaceItem
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()
        place = Place.objects.filter(host=host).first
        context.update({
            'user': self.request.user,
            'host': host,
            'places': place
        })

        return context


place_item_list = PlaceItemListView.as_view()


class PlaceItemDetailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'admin/place/place_item_detail.html'
    model = PlaceItem
    form_class = PlaceItemModelForm
    success_url = reverse_lazy('place_list_item')
    success_message = _("正常に更新されました")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()
        context.update({
            'user': self.request.user,
            'host': host,
        })

        return context


place_item_detail = PlaceItemDetailView.as_view()
