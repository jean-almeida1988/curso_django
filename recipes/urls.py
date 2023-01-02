from django.contrib import admin
from django.urls import path

from recipes.views import about, contact, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact),
]