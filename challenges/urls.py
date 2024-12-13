from django.urls import path
from . import views

#these are the url patterns for this app named challenges
urlpatterns = [
    path('<month>', views.monthly_challenges),  # these angular brackets provides a dyanmic path segment
]
