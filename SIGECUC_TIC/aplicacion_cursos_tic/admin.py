from django.contrib import admin
from models import Persona
#Administrador no es necesario
#from models import Administrador
from models import MasterTeacher
from models import HistorialLaboral
#from models import HistorialAcademico
from models import Inscrito
from models import LeaderTeacher
from models import AreaFormacion
from models import ActividadEvaluacion
from models import Curso
from models import Cohorte
from models import Calificacion
from models import LeaderTeacher_Cohorte


#Recarga la lista de persona y se podra ver tres columnas Nombres,y E-mail.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
         'primer_apellido', 'segundo_apellido')
    search_fields = ('identificacion', 'primer_nombre', 'segundo_nombre',
         'primer_apellido', 'segundo_apellido')

#REGISTRO DE MODELOS EN EL SITIO DE ADMINISTRACION
#DEL ADMINISTRADOR

# Register your models here.
admin.site.register(Persona, PersonaAdmin)
#Administrador no es necesario
#admin.site.register(Administrador)


#Recarga la lista de curso.


class MasterTeacherAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
    'primer_apellido', 'segundo_apellido')
    #search_fields = ('identificacion', 'primer_nombre') #verificar no busca
admin.site.register(MasterTeacher, MasterTeacherAdmin)
#admin.site.register(HistorialLaboral)
admin.site.register(Inscrito)


class LeaderTeacherAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'primer_nombre', 'segundo_nombre',
    'primer_apellido', 'segundo_apellido', 'fecha_nacimiento', 'sexo',
    'ciudad_nacimiento', 'pais_nacimiento', 'ciudad_residencia',
     'pais_residencia', 'ciudad_labora', 'departamento_labora',
     'fecha_activacion')
#remporal no busca datos con persona
    search_fields = ('ciudad_labora', 'departamento_labora')

admin.site.register(LeaderTeacher, LeaderTeacherAdmin)


#Recarga la lista de Area_formacion.
class Area_formacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
admin.site.register(AreaFormacion, Area_formacionAdmin)


#Recarga la lista de curso.
class ActividadEvaluacionAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'peso')
    search_fields = ('descripcion', 'peso')
admin.site.register(ActividadEvaluacion, ActividadEvaluacionAdmin)


#Recarga la lista de curso.
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'descripcion')
    search_fields = ('nombre', 'estado')
    filter_horizontal = ('actividad_evaluacion',)
admin.site.register(Curso, CursoAdmin)


#Recarga la lista de cohorte.
class CohorteAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'fecha_fin', 'nombre_curso',
    'id_Master_Teacher', 'nombre_Master_Teacher')
    #search_fields = ('nombre', 'estado')
admin.site.register(Cohorte, CohorteAdmin)
admin.site.register(Calificacion)
admin.site.register(LeaderTeacher_Cohorte)



