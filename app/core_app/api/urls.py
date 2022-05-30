from django.urls import include, path

from . import routers

urlpatterns = [
    path("1.0/", include(routers)),
]
