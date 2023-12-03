from django.contrib import admin

from home.models import Gnev

@admin.register(Gnev)
class GnevAdmin(admin.ModelAdmin):
   list_display = ["name", "color", "years", "power"]
   list_filter = ["power"]