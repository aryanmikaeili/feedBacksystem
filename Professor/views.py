from django.shortcuts import render
from .models import Professor
def professor_view(request, id):
    obj = Professor.objects.get(id=id)
    context = {
        "object" : obj
    }
    return render(request, "professor/detail.html", context)
# Create your views here.

# Create your views here.
