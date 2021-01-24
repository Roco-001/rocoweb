"""rococv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from core import views as viewcore
from pages.views import PostListView
from pages import views as viewpages
from contact import views as viewcontact
from core.views import PrintCvPdf


urlpatterns = [

    
    #vistas del core
    path('', viewcore.home, name="home"),
    path('about/', viewcore.about, name="about"),
    path('reference/', viewcore.reference, name="reference"),    
    path('employement/', viewcore.employement, name="employement"),
    path('education/', viewcore.education, name="education"), 
    path('download/', PrintCvPdf.as_view(), name="print_to_pdf"),  
    #path('download/', viewcore.print_to_pdf, name="print_to_pdf"), 
    
    #vistas del blog
    path('blog/', PostListView.as_view(), name="blogs"),
    path('blog/<int:post_id>/<slug:post_slug>/', viewpages.blog, name="blog"),
    path('blog/category/<int:category_id>/<slug:category_slug>/', viewpages.category, name="category"),

    #Vistas del Contact
    path('contact/', viewcontact.contact, name="contact"), 

    #Vistas del ckeditor uploader
    path('ckeditor/', include('ckeditor_uploader.urls')), 
   
    path('admin/', admin.site.urls),
]


#Nos permite servir ficheros estaticos
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)