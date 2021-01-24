from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import About, Employement, Education, Curso, Skill, Reference
from .utils import render_to_pdf
from django.views.generic import View

# Create your views here.
#Vista para la pagina Home y ordenar productos en la portada
def home(request):
    return render(request, "core/home.html")

def about(request):
    about = About.objects.all()
    return render(request, "core/about.html", {'about': about})

def reference(request):
    referencias = Reference.objects.all()
    return render(request, "core/reference.html",  {'referencias': referencias})

def employement(request):
    employements = Employement.objects.all().order_by('-tiempo')
    return render(request, "core/employement.html", {'employements': employements})

def education(request):
    educations = Education.objects.all().order_by('-tiempo')
    cursos = Curso.objects.all().order_by('-tiempo')
    skills = Skill.objects.all()
    return render(request, "core/education.html", {'educations': educations, 'cursos': cursos, 'skills': skills,} )


"""
def print_to_pdf(request):
    about = About.objects.all()
    educations = Education.objects.all().order_by('-tiempo')
    cursos = Curso.objects.all().order_by('-tiempo')
    skills = Skill.objects.all()
    employements = Employement.objects.all().order_by('-tiempo')
    referencias = Reference.objects.all()
    return render(request, "core/index_pdf.html",{
        'about': about, 'educations': educations, 'cursos': cursos, 'skills': skills,'employements': employements, 
        'referencias': referencias})
"""

class PrintCvPdf(View):

    def get(self, request, *args, **kwargs):
        about = About.objects.all()
        educations = Education.objects.all().order_by('-tiempo')
        cursos = Curso.objects.all().order_by('-tiempo')
        skills = Skill.objects.all()
        employements = Employement.objects.all().order_by('-tiempo')
        referencias = Reference.objects.all()
        data = {
            'about': about,
            'educations': educations,
            'cursos': cursos, 
            'skills': skills,
            'employements': employements, 
            'referencias': referencias
        }
        pdf = render_to_pdf('core/index_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    




