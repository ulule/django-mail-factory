from django.conf.urls import include, url
from django.contrib import admin
from django.urls import re_path

urlpatterns = [
    re_path(r"^mail_factory/", include("mail_factory.urls")),
    re_path(r"^admin/", admin.site.urls),
]
