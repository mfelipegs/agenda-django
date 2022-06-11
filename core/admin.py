from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'event_data', 'local', 'creation_data')
	list_filter = ("user", "event_data",)

admin.site.register(Evento, EventoAdmin)
