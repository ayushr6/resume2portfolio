from rest_framework import serializers

from .models import User, Bio, TechnicalSkills, QualificationDetails, Projects

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'Username', 'Name', 'Email', 'LinkedInURL', 'GitHubURL')

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = ('BioID', 'UserID', 'Role', 'AboutMe')

# serializers.py

class TechnicalSkillsSerializer(serializers.ModelSerializer):
    UserID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = TechnicalSkills
        fields = ('SkillID', 'UserID', 'CodingLanguages', 'OtherTechnologies')
        
class QualificationDetailsSerializer(serializers.ModelSerializer):
    UserID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = QualificationDetails
        fields = ('QualificationID', 'UserID', 'DegreeName', 'YearFrom', 'YearTo', 'CGPA', 'CollegeSchoolName')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('ProjectID', 'UserID', 'ProjectTitle', 'ProjectLink', 'ProjectDescription')


class UserDetailsSerializer(serializers.ModelSerializer):
    bio = BioSerializer()
    technical_skills = TechnicalSkillsSerializer(many=True)
    qualification_details = QualificationDetailsSerializer(many=True)
    projects = ProjectsSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'Username', 'Name', 'Email', 'LinkedInURL', 'GitHubURL', 'bio', 'technical_skills', 'qualification_details', 'projects')
