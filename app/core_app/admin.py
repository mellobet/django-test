from django.contrib import admin

from .models import Atendee, Event


@admin.register(Event)
class Event(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Atendee)
class Atendee(admin.ModelAdmin):
    search_fields = (
        "first_name",
        "last_name",
    )
