from django import forms
from .models import User, Bio, TechnicalSkills, QualificationDetails, Projects



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Name', 'Email', 'LinkedInURL', 'GitHubURL']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders for existing values
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = getattr(self.instance, field_name)


class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['Role', 'AboutMe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders for existing values
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = getattr(self.instance, field_name)





class TechnicalSkillsForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkills
        fields = ['CodingLanguages', 'OtherTechnologies']

class QualificationDetailsForm(forms.ModelForm):
    class Meta:
        model = QualificationDetails
        fields = ['DegreeName', 'YearFrom', 'YearTo', 'CGPA', 'CollegeSchoolName']

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['ProjectTitle', 'ProjectLink', 'ProjectDescription']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders for existing values
        self.fields['ProjectTitle'].widget.attrs['placeholder'] = self.instance.ProjectTitle
        self.fields['ProjectLink'].widget.attrs['placeholder'] = self.instance.ProjectLink
        self.fields['ProjectDescription'].widget.attrs['placeholder'] = self.instance.ProjectDescription

