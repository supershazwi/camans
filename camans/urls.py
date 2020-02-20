from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('baby/', include('baby.urls', namespace='baby')),
    path('adult/', include('adult.urls', namespace='adult')),
    path('admin/', admin.site.urls),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]