from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from logica.leader_teacher_mediator import LeaderTeacherMediator

def pagina_leader_teacher_informacion_personal(request):
	
	leader_teacher_mediator = LeaderTeacherMediator()
	if request.method == "POST":
		#Opcion 2 para actualizar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,2)
	else:
		#Opcion 1 para mostrar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,1)
	
def pagina_consulta_cursos_calificados(request):
	leader_teacher_mediator = LeaderTeacherMediator()
	return leader_teacher_mediator.calificaciones_task(request=request,option=1)

def pagina_leader_teacher_descripcion_calificacion(request,cohorte_id):
	leader_teacher_mediator = LeaderTeacherMediator()
	return leader_teacher_mediator.calificaciones_task(request=request,cohorte_id=cohorte_id,option=2)

def pagina_generar_certificado(request):
	return render_to_response('certificado.html',context_instance=RequestContext(request))



def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


