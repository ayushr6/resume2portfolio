from django.db import models

# Create your models here.

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=120)
    bio= models.TextField()
    # completed = models.BooleanField(default=False)

    def _str_(self):
        return self.name
