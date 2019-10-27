from django.contrib import admin

from .models import Aula
from .models import	Gafas
from .models import Juego
from .models import Usuario
from .models import Reserva



class ReservaInLine(admin.StackedInline):
	model = Reserva
	extra = 3

class GafasInLine(admin.StackedInline):
	model = Gafas
	extra = 3

class AulaInLine(admin.StackedInline):
	model = Aula
	extra = 3

class JuegoInLine(admin.StackedInline):
	model = Juego
	extra = 3

class UsuarioInLine(admin.StackedInline):
	model = Usuario
	extra = 3



class AulaAdmin(admin.ModelAdmin):
	exclude = []
	inlines = [GafasInLine]

class GafasAdmin(admin.ModelAdmin):
	exclude = []
	

class JuegoAdmin(admin.ModelAdmin):
	exclude = []
	

class UsuarioAdmin(admin.ModelAdmin):
	exclude = []
	

class ReservaAdmin(admin.ModelAdmin):
	exclude = []
	list_display = ('id_gafas','id_juego','id_usuario','fecha_inicio','fecha_fin')
	
	




admin.site.register(Aula, AulaAdmin)
admin.site.register(Gafas, GafasAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reserva, ReservaAdmin)