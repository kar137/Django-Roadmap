from django.urls import path
from . import views

#these are the url patterns for this app named challenges
urlpatterns = [
    path('', views.month_list, name="index"),   #when no path written it reloads this page
    path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenges, name="month-challenge"),  # these angular brackets provides a dyanmic path segment and str: is a path converter
]
