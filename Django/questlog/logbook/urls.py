from django.urls import path #Helper to define url patterns
from .import views #import the views from app
urlpatterns = [
    path("",views.home, name = "home"),
    path("quests/", views.quest_list, name = "quest-list"),#url for the quest list
    path("servants/",views.servant_list,name = "servant-list"), #url for servant list
    path("constructs/",views.construct_list,name="construct-list"),
    path("quests/create/",views.create_quest,name="create-quest"),
    #tell django to send any unique number to views:
    path("quest/<int:pk>/",views.quest_detail,name="quest-detail")
]