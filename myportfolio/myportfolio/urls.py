from django.contrib import admin
from django.urls import path
from projects.views import home
from projects.views import contact
from projects.views import about
from projects.views import projects


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact),
    path('projects/', projects),
    path('about/', about),
]

