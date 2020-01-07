from django.db import models
from Professor.models import Professor
# Create your models here.


class Course(models.Model):
    CourseID = models.PositiveIntegerField(null=False, blank=False)
    GroupID = models.PositiveSmallIntegerField(null=False, blank=False)
    Name = models.CharField(null=False, blank=False, max_length=100)
    Professor = models.ManyToManyField(Professor, blank=False)
    class Meta:
        ordering = ['CourseID']
        unique_together = (('CourseID', 'GroupID'),)

