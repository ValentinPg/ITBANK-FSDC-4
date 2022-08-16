from django.contrib import admin
from homebank.models import SolicitudesPrestamos

class SolicitudAdmin(admin.ModelAdmin):
    pass
admin.site.register(SolicitudesPrestamos,SolicitudAdmin)
