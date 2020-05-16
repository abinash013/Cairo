from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name="homepage"),
    path('index/<str:dname>', views.index, name="index"),
]
