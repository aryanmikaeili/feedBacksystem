from django.db import models

# Create your models here.


class Course(models.Model):
    CourseID = models.PositiveIntegerField(null=False, blank=False)
    GroupID = models.PositiveSmallIntegerField(null=False, blank=False)
    Name = models.CharField(null=False, blank=False, max_length=100)
    Grade = models.PositiveIntegerField(null=False, blank=False)
