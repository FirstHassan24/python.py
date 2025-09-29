from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('state/<slug:state>/', views.details, name='details'),

    ]