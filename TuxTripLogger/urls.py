from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logger/", views.logger, name="logger"),
    path("logs/", views.logs, name="logs"),
    path("demo/", views.demo, name="demo"),
]
