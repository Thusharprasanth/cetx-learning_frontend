from courses.models import Course
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def store(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(request , 'store/store.html', context)