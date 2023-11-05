from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json
from .models import Course


def index(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.all()
    
    return HttpResponse(courses)
