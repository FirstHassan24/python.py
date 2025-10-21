from django.urls import path
from . import views

# This list holds all the URL patterns for the 'logbook' app.
# Django will look through this list in order to find a match for an incoming URL.
urlpatterns = [
    # The root URL of the app (e.g., '/logbook/'). Calls the 'home' view.
    path("", views.home, name="home"),

    # --- Quest URLs ---
    # URL for the list of all quests. Calls the 'quest_list' view.
    path("quests/", views.quest_list, name="quest-list"),
    # URL for creating a new quest. Calls the 'create_quest' view.
    path("quests/create/", views.create_quest, name="create-quest"),
    # Dynamic URL for a single quest's detail page. 
    # It captures an integer from the URL (the primary key) and passes it to the 'quest_detail' view.
    path("quests/<int:pk>/", views.quest_detail, name="quest-detail"),

    # --- Servant URLs ---
    # URL for the list of all servants. Calls the 'servant_list' view.
    path("servants/", views.servant_list, name="servant-list"),
      #URL for summoning servants. calls the summon_servant view
    path("summon/servant",views.summon_servant,name="summon-servant"),
    #create the url then capture the int(pk) and pass it to the views: 
    path("servant/<int:pk>/",views.servant_details,name="servant-details"),
    #sends the pk to view to run the delete function:
    path("delete/<int:pk>/",views.delete_servant,name="delete-servant"),

    # --- Construct URLs ---
    # URL for the list of all constructs. Calls the 'construct_list' view.
    path("constructs/", views.construct_list, name="construct-list"),
]