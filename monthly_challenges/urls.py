from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include('challenges.urls')),  #this helps to connect the project main setup to the app url
]
