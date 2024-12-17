from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=40)
    price = models.CharField(max_length=15)
    discount= models.IntegerField()
    duration = models.DurationField()
    author_name = models.CharField(max_length= 40)

    def __str__(self):
        return self.name