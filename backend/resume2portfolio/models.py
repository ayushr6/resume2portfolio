# models.py

from django.db import models

class User(models.Model):
    # Django automatically creates 'id' field as the primary key
    Username = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(default='', unique=True)
    LinkedInURL = models.URLField(blank=True, null=True)
    GitHubURL = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.Username

class Bio(models.Model):
    BioID = models.AutoField(primary_key=True)
    UserID = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bio')
    Role = models.CharField(max_length=100)
    AboutMe = models.TextField()
    
    def __str__(self):
        return f"{self.UserID.Username}'s Bio"

class TechnicalSkills(models.Model):
    SkillID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='technical_skills')
    CodingLanguages = models.TextField()
    OtherTechnologies = models.TextField()
    
    def __str__(self):
        return f"{self.UserID.Username}'s Technical Skills"

class QualificationDetails(models.Model):
    QualificationID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qualification_details')
    DegreeName = models.CharField(max_length=100)
    YearFrom = models.PositiveIntegerField()
    YearTo = models.PositiveIntegerField()
    CGPA = models.FloatField()
    CollegeSchoolName = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.UserID.Username}'s Qualification Details"

class Projects(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    ProjectTitle = models.CharField(max_length=200)
    ProjectLink = models.URLField(blank=True, null=True)
    ProjectDescription = models.TextField()
    
    def __str__(self):
        return f"{self.UserID.Username}'s Project: {self.ProjectTitle}"
