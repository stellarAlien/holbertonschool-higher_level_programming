#!/usr/bin/python3
from django.contrib import admin
from django.urls import path
import .views import HomePageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="homepage"),
]