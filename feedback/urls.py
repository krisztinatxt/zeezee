from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.comment, name='feedback'),
]