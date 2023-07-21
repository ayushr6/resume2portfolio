from django.contrib import admin


from .models import user

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

# Register your models here.

admin.site.register(user, UserAdmin)