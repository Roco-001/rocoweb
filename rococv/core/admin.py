from django.contrib import admin
from .models import About, Employement, Education, Curso, Skill, Reference

class AboutProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name',  'created' , 'updated')

   
    
#
class EmployementProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tiempo', 'empresa',  'cargo' , 'created')


class EducationProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'universidad',  'created' , 'updated')

class CursoProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'academia',  'created' , 'updated')

class SkillProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'porcentaje', 'created' , 'updated')


class ReferenceProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created' , 'updated')





# Register your models here.
admin.site.register(About, AboutProject)

admin.site.register(Employement, EmployementProject)


admin.site.register(Education, EducationProject)
admin.site.register(Curso, CursoProject)
admin.site.register(Skill, SkillProject)

admin.site.register(Reference,ReferenceProject)
