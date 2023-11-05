from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse, Http404
from .models import Course, Category


def index(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.all()
    
    return render(request, 'courses.html', {'courses': courses})


def show_course(request: HttpRequest, course_id: int) -> HttpResponse:
    # # OPTION 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    # except Course.DoesNotExist as exc:
    #     raise Http404()

    course = get_object_or_404(Course, pk=course_id)

    return render(request, 'detail.html', {'course': course})


def show_category(request: HttpRequest, category_id: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'category': category,
        'courses': category.course_set.all(),
    }

    return render(request, 'category.html', context)