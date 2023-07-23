from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Bio, TechnicalSkills, QualificationDetails, Projects
from .serializers import UserSerializer, BioSerializer, TechnicalSkillsSerializer, QualificationDetailsSerializer, ProjectsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BioViewSet(viewsets.ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioSerializer

class TechnicalSkillsViewSet(viewsets.ModelViewSet):
    queryset = TechnicalSkills.objects.all()
    serializer_class = TechnicalSkillsSerializer

class QualificationDetailsViewSet(viewsets.ModelViewSet):
    queryset = QualificationDetails.objects.all()
    serializer_class = QualificationDetailsSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
