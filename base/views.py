from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def my_custom_not_found_view(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, 'error_handlers/404.html', status=404)