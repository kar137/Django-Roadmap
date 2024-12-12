from django.urls import path
from . import views

#these are the url patterns for this app named challenges
urlpatterns = [
    path('january', views.index),
]
