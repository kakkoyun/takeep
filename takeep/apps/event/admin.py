from django.contrib import admin
from apps.event.models import Event, Participant, EventReport

admin.site.register(Event)
admin.site.register(Participant)
admin.site.register(EventReport)
