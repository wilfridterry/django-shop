from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.show_course, name='show'),
    path('category/<int:category_id>', views.show_category, name='category'),
]