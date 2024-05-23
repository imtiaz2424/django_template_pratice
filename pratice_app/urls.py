from django.urls import path
# from pratice_app.views import home
# from pratice_app import views
from . import views

urlpatterns = [
   
    path('', views.home),
]
