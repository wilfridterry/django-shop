from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop.index'),
    # path('create', views.create, name='shop.create', method='post')
]