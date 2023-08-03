from django.shortcuts import render

from rest_framework import viewsets
from django.forms import formset_factory, modelformset_factory, inlineformset_factory

from django.http import JsonResponse
from .models import User, Bio, TechnicalSkills, QualificationDetails, Projects
from .serializers import UserSerializer, BioSerializer, TechnicalSkillsSerializer, QualificationDetailsSerializer, ProjectsSerializer,UserDetailsSerializer


from django.shortcuts import render, redirect
from .forms import UserForm, BioForm, TechnicalSkillsForm, QualificationDetailsForm, ProjectsForm

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


# def index(request):

#     return render(request,'index.html')

class UserDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    lookup_field = 'id'




def create_user(request, user_id=None):
    if user_id:
        # If user_id is provided, fetch the user instance from the database
        user_instance = User.objects.get(pk=user_id)
    else:
        user_instance = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('bio_form', user_id=user_id) 
    else:
        form = UserForm(instance=user_instance)

    return render(request, 'user_form.html', {'form': form})




def bio_form(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = BioForm(request.POST, instance=user.bio)
        if form.is_valid():
            form.instance.UserID = user
            form.save()
            return redirect('projects_form', user_id=user_id) 

    else:
        form = BioForm(instance=user.bio)

    return render(request, 'bio_form.html', {'form': form})




def delete_project(request, project_id):
    try:
        project = Projects.objects.get(pk=project_id)
        project.delete()
        return JsonResponse({'success': True})
    except Projects.DoesNotExist:
        return JsonResponse({'success': False})






def projects_form(request, user_id):
    user = User.objects.get(pk=user_id)

    ProjectsFormSet = modelformset_factory(Projects, form=ProjectsForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = ProjectsFormSet(request.POST, queryset=Projects.objects.filter(UserID=user), prefix='projects')
        if formset.is_valid():
            formset.save()
            return redirect('success_page')
        else:
            print("Invalid formset:")
            print(formset.errors)
    else:
        formset = ProjectsFormSet(queryset=Projects.objects.filter(UserID=user), prefix='projects')

    return render(request, 'projects_form.html', {'formset': formset, 'user_id': user_id})



def back_to_user_form(request):
    # Replace 'your_user_id' with the actual user ID or relevant logic to get the user ID
    user_id = 'your_user_id'
    return redirect('user_form', user_id=user_id)