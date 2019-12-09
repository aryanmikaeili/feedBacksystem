from django.shortcuts import render
from Student.forms import UserSignUpForm, StudentSignUpForm
from Professor.forms import ProfessorSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from Professor.models import Professor
from Student.models import Student
# Create your views here.


def signup(request):
    print(request.method, request.body)
    registered = False
    if request.method == 'POST':
        if 'Field' in request.FILES:
            user_form = UserSignUpForm(data=request.POST)
            prof_form = ProfessorSignUpForm(data=request.POST)
            profile_form = StudentSignUpForm()
            if user_form.is_valid() and prof_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = prof_form.save(commit=False)
                profile.user = user
                profile.ProfID = user.username
                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
            else:
                print(user_form.errors, prof_form.errors)

        else:
            user_form = UserSignUpForm(data=request.POST)
            profile_form = StudentSignUpForm(data=request.POST)
            prof_form = ProfessorSignUpForm()
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.StudentID = user.username
                if 'profile_pic' in request.FILES:
                    print('found it')
                    profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)

    else:
        user_form = UserSignUpForm()
        profile_form = StudentSignUpForm()
        prof_form = ProfessorSignUpForm()


    print("AWLIIIII", registered, user_form, profile_form, prof_form)
    #return HttpResponse("user logged in")
    return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'prof_form':prof_form,'registered':registered})


def user_login(request):
    print(request.method)
    print(request.body)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if Student.objects.get(StudentID=username) != None:
                    print("hey")
                    login(request, user)
                    #return HttpResponseRedirect("/signup")

                    return HttpResponse("Student-Login")
                else:
                    login(request, user)
                    return HttpResponse("Professor-Login")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'index.html', {})