from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # API
    path("api/", include("core_app.api.urls")),
]
