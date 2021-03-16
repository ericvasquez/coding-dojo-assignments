from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("destroy_session", views.destroy_session),
    path("destroy_visits", views.destroy_visits),
    path("plusTwo", views.plusTwo),
    path("addNumber", views.addNumber)
]
