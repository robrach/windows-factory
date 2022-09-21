from django.contrib import admin
from .models import *


@admin.register(Window)
class WindowAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
