from django.contrib import admin
from django.urls import path,include

from . import views
app_name = "fidpha"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("resume/", views.clients_resume, name="resume"),

    path("", views.client_dashboard, name="client_dashboard"),
    path("client/details/", views.client_details, name="client_details"),

]