from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^parties/$', views.PartyList.as_view()),
]
