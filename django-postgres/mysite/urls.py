from django.urls import path
from counter.views import home

urlpatterns = [path("", home)]
