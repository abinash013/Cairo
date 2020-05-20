from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name="homepage"),
    path('index/<str:dname>', views.index, name="index"),
    path('signin', views.signin, name="signin"),
    path('signinprocess', views.siginprocess, name="signinprocess"),
    path('login', views.login, name="login"),
]
