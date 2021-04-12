from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    courses= Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'index.html', context)

def addCourse(request):
    errors = Course.objects.course_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        if request.method == "POST":
            Course.objects.create(
                name= request.POST['name'],
                description= request.POST['description'],
            )
            return redirect('/')
        return redirect('/')

def deleteCourse(request, courseId):
    if request.method == "GET":
        context = {
            "course": Course.objects.get(id= courseId)
        }
        return render(request, 'delete.html', context)

    if request.method == "POST":
        course= Course.objects.get(id=courseId)
        course.delete()
        return redirect('/')
# Create your views here.
