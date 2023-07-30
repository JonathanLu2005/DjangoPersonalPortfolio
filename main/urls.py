from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path("home/", views.home, name="home"),

path("education/", views.education, name="education"),

path("experience/", views.experience, name="experience"),

path("", views.signup, name="signup"),

path("login/", views.login, name="login"),
]

urlpatterns += staticfiles_urlpatterns()