from django.contrib import admin as admin_nongeo
from . import models
from django.contrib.auth import get_user_model
from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.unregister(get_user_model())

admin.site.register(models.Party, admin.OSMGeoAdmin)
admin.site.register(models.Genre)
