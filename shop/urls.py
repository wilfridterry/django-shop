from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop.index'),
    path('<int:course_id>', views.show_course, name='shop.show'),
    path('category/<int:category_id>', views.show_category, name='shop.category'),
]