from django.db import models
#from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=100, 
        verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    #content = RichTextField(verbose_name= "Contenido",  null=True, blank=True)       
    content = RichTextUploadingField(verbose_name= "Contenido",  null=True, blank=True) 

    image = models.ImageField(upload_to="category", null=True, blank=True,
        verbose_name="Imagen")

    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    #content = RichTextField(verbose_name= "Contenido")
    content = RichTextUploadingField(verbose_name= "Contenido",  null=True, blank=True) 

    published = models.DateTimeField(default=now,
        verbose_name="Fecha de publicación")
    image = models.ImageField(upload_to="blog", null=True, blank=True,
        verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
        verbose_name="Autor")
    categories = models.ManyToManyField(Category, 
        verbose_name="Categorías")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title