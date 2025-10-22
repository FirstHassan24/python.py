#import the path so we can start linking other files to url:
from django.urls import path
#import the views so we can link it to a url"
from . import views
# Define all the routes for the logbook app
urlpatterns = [
    #    # Home page that lists all servants
    path("",views.servant_list,name="servant-list"),
        # Page to summon (create) a new servant
    path("new/",views.servant_create,name="servant-create"),
    # Update page (Update) — <pk> is the id in the database:
    path("<int:pk/edit/",views.servant_update,name="servant-update"),

    ]
