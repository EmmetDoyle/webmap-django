# from django.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point

from django.contrib.gis.db import models
from django.contrib.gis import geos
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Genre(models.Model):
    name = models.CharField(max_length=25)

class Party(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre)
    location = models.PointField()

