from django.urls import path

from djapps.users.views import custom_login, custom_logout, home

urlpatterns = [
    path("", home,name='home'),
    path("login/", custom_login, name='login'),
    path("logout/", custom_logout, name='logout'),
]
