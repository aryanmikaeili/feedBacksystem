from django.shortcuts import render
from .models import Student
# Create your views here.

def student_view(request, id):
    obj = Student.objects.get(id=id)
    context = {
        "object" : obj
    }
    return render(request, "student/detail.html", context)
