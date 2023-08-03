"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# from . import views
from rest_framework import routers
# from resume2portfolio import views
from resume2portfolio.views import UserViewSet, BioViewSet, TechnicalSkillsViewSet, QualificationDetailsViewSet, ProjectsViewSet,UserDetailsSerializer
from resume2portfolio.views import UserDetailsViewSet,create_user,bio_form,projects_form, delete_project,back_to_user_form
# Create a router and register our viewsets with it.
router =routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bio', BioViewSet)
router.register(r'technical-skills', TechnicalSkillsViewSet)
router.register(r'qualification-details', QualificationDetailsViewSet)
router.register(r'projects', ProjectsViewSet)
router.register(r'user-details', UserDetailsViewSet, basename='user-details')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",index),
    path('api/', include(router.urls)),
    path('create_user/', create_user, name='create_user'),
    
    path('update_user/<int:user_id>/', create_user, name='update_user'),
    path('bio_form/<int:user_id>/', bio_form, name='bio_form'),
    path('projects_form/<int:user_id>/', projects_form, name='projects_form'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
    path('back_to_user_form/', back_to_user_form, name='back_to_user_form'),
]
