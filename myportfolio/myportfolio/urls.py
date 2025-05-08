from django.contrib import admin
from django.urls import path
from projects.views import home
from projects.views import contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact),
]

