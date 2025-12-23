from django.contrib import admin
from ferreteria.models import *


#admin.site.register(Sector)

@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "nro_sector", "email_sector", "fecha_de_creacion")
    list_display_links = ("nombre",)
    search_fields = ("nro_sector",)
    list_filter = ("fecha_de_creacion",)
    ordering = ("nro_sector", "nombre")
    readonly_fields = ("fecha_de_creacion",)