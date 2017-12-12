from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from django.forms import ValidationError
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from rest_framework import generics
from app.serializers import PartySerializer
from app.models import Party, Genre
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from . import forms

class PartyList(generics.ListAPIView):
    serializer_class = PartySerializer

    def get_queryset(self):
        longitude = float(self.request.query_params['longitude'])
        latitude = float(self.request.query_params['latitude'])
        radius = 10
        point = Point(longitude, latitude)

        return Party.objects.filter(location__distance_lt=(point, Distance(km=radius)))
