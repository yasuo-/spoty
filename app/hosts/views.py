from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from .models import Host, Place, PlaceItem
from .filters import PlaceFilter
from .forms import (
    HostModelForm,
    PlaceModelForm,
    PlaceItemModelForm
)

from app.address.models import Prefecture, City, Address


class CreateHostView(CreateView):
    model = Host
    form_class = HostModelForm
    template_name = 'hosts/new.html'
    # success_url = reverse_lazy('hosts:place_create')
    success_message = _("正常に作成されました")

    def get_success_url(self):
        return reverse_lazy('hosts:place_create')


host_create = CreateHostView.as_view()


class PlaceHostView(CreateView):
    model = Place
    form_class = PlaceModelForm
    template_name = 'hosts/place_new.html'
    success_url = reverse_lazy('hosts:place_list')
    success_message = _("正常に作成されました")

    def get_context_data(self, *args, **kwargs):
        context = super(PlaceHostView, self).get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()
        if host is None:
            context.update({
                'user': self.request.user,
                'host': None,
            })
        else:
            context.update({
                'user': self.request.user,
                'host': host,
            })
        return context


place_create = PlaceHostView.as_view()


class PlaceListView(LoginRequiredMixin, FilterView):
    template_name = 'hosts/place_list.html'
    model = Place
    filterset_class = PlaceFilter
    queryset = Place.objects.all().order_by('-created_at')

    strict = False
    paginate_by = 10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        host = Host.objects.filter(user=self.request.user).order_by('created_at').first()

        context.update({
            'user': self.request.user,
            'host': host,
        })

        return context

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)

place_list = PlaceListView.as_view()


class PlaceDetailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'hosts/place_detail.html'
    model = Place
    form_class = PlaceModelForm
    success_url = reverse_lazy('hosts:place_list')
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


class PlaceItemCreateView(CreateView):
    model = PlaceItem
    form_class = PlaceItemModelForm
    template_name = 'hosts/place_item_new.html'
    success_url = reverse_lazy('hosts:place_list')
    success_message = _("正常に作成されました")

    def get_context_data(self, *args, **kwargs):
        context = super(PlaceItemCreateView, self).get_context_data(**kwargs)
      #  place = Place.objects.get(id=self.kwargs['pk'])
        context.update({
            'user': self.request.user,
      #       'place': place
        })
        return context


place_item_create = PlaceItemCreateView.as_view()
