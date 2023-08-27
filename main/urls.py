from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'main'

urlpatterns = [
    path(route='', view=views.Home.as_view(), name='home'),
]