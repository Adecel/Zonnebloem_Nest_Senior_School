from django.db import models
from django.urls import reverse

from Matric.validators import image_validation_extension,video_validation_extention

# Create your models here.
class MatricYear(models.Model):
    matric_year = models.IntegerField()

class Matriculant(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    year = models.ForeignKey(MatricYear, on_delete=models.CASCADE, related_name="year")
    id_photo =  models.ImageField(upload_to='images/',validators=[image_validation_extension])

    def get_absolute_url(self):
        return reverse('Matric:matric.html')

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.id_photo}"
