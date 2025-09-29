from django.urls import path
from . import views
# this is used to connect view to the url so when someone click on it or types it it will rederict them to over her
urlpatterns = [
    path("", views.home, name="home"),
    path("todo/", views.todos, name="todo")
]