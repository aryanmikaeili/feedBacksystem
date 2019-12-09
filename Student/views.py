from django.shortcuts import render
from .models import Student
# Create your views here.

def student_view(request, id):
    print(type(id))
    obj = Student.objects.get(StudentID=id)
    context = {
        "object" : obj
    }
    return render(request, "student/detstu.html", context)
