"""ElegantVision URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('showcase.urls')),  # Include URLs from the showcase app
]
