from django.contrib import admin
from .models import User, Bio, TechnicalSkills, QualificationDetails, Projects
# admin.site.register(User)
admin.site.register(Bio)
admin.site.register(TechnicalSkills)
admin.site.register(QualificationDetails)
admin.site.register(Projects)



class UserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'LinkedInURL')

# Register your models here.

admin.site.register(User, UserAdmin)