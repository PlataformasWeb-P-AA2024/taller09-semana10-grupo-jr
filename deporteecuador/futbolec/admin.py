from django.contrib import admin
from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos


class EquipoFutbolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'username_twitter',)
    search_fields = ('nombre',)

# admin.site
admin.site.register(EquipoFutbol, EquipoFutbolAdmin)


class JugadorAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo_futbol')
    search_fields = ('nombre', 'equipo_futbol')
admin.site.register(Jugador, JugadorAdmin)



class CampeonatoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'auspiciante',)
    search_fields = ('nombre',)

admin.site.register(Campeonato, CampeonatoAdmin)


class EquiposCampeonatosAdmin(admin.ModelAdmin):
    list_display = (
'año',
'equipo_futbol',
'campeonato',
    )
    search_fields = ('equipo_futbol',)
    

admin.site.register(CampeonatoEquipos, EquiposCampeonatosAdmin)
