from django import forms
from .models import Persona
from .models import HistorialLaboral
from .models import HistorialAcademico
from .models import ZonaInstitucionEducativa
from .models import CaracterTecnica
from .models import EtniaEducativa
from .models import GradosEscolares
from .models import Inscrito
from .models import Persona


#Clas LoginForm
#Es la clase relacionada con el formulario de login.html
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())


class InscripcionPersonaForm(forms.ModelForm):
	class Meta:
		model = Persona

class HistorialAcademicoForm(forms.ModelForm):
	#zona_institucion_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=ZonaInstitucionEducativa.objects.all())
	#caracter_tecnica = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=CaracterTecnica.objects.all())
	#etnia_educativa = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=EtniaEducativa.objects.all())
	#grado_escolar = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=True,
		#queryset=GradosEscolares.objects.all())
	class Meta:
		model = HistorialAcademico

class HistorialLaboralForm(forms.ModelForm):
	class Meta:
		model = HistorialLaboral


class Persona_MasterTeacherForm(forms.ModelForm):
	class Meta:
		model = Persona




		