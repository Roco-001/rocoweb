from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre(s)")
    lastname = models.CharField(max_length=100, verbose_name="Apellido(s)")
    enamil = models.EmailField(max_length=100, verbose_name="Email")
    direccion = models.CharField(max_length=300, verbose_name="Dirección", blank= True, null= True, )
    phone = models.CharField(max_length=300, verbose_name="Teléfono" , blank= True, null= True,)
    descripcion = RichTextField(verbose_name= "Descripción")
    image = models.ImageField(verbose_name= 'Adjunta la Imagen del About', upload_to = 'about')
    url = models.URLField(verbose_name="Enlace a Linkedin", max_length=200, null=True, blank=True)    
   

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Acerca de"
        verbose_name_plural = "Acerca de"
        

    def __str__(self):
        return self.name


class Employement(models.Model):
    tiempo = models.CharField(max_length=100, verbose_name="Tiempo")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    actividades = RichTextField(verbose_name= "Actividades")
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return self.empresa

class Education(models.Model):
    tiempo = models.CharField(max_length=100, verbose_name="Tiempo")
    titulo = models.CharField(max_length=100, verbose_name="Titulo Obtenido")
    universidad = models.CharField(max_length=100, verbose_name="Universidad")
   
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Educacion"
        verbose_name_plural = "Educacion"

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    tiempo = models.CharField(max_length=100, verbose_name="Tiempo")
    name = models.CharField(max_length=100, verbose_name="Nombre del Curso")
    academia = models.CharField(max_length=100, verbose_name="Academia")
    certificacion = models.CharField(max_length=100, verbose_name="Id de Certificacion",blank= True, null= True)
   
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        

    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Habilidad")
    porcentaje = models.CharField(max_length=100, verbose_name="Porcentaje")
  
   
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    referencia = models.CharField(max_length=100, verbose_name="Telefono")
   
    
  
   
   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Referencia"
        verbose_name_plural = "Referencias"

    def __str__(self):
        return self.name