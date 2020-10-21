from django.db import models

# Create your models here.
class Upload(models.Model):
    name = models.CharField(max_length=15)
    PersonFace = models.ImageField(upload_to='capture/')

    def __str__(self):
        return self.name