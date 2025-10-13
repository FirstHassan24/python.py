from django.shortcuts import render,redirect,get_object_or_404
from .models import Fgo
from .forms import Summon_Servant
from django.http import HttpResponse
#bring the api file so views can use it:
from .services import get_servant

# Create your views here.
#create a function that handles the form logic:
def summon(request):
    #handle the logic if the user input something:
    if request.method =="POST":
        #link the users request with the form:
        form = Summon_Servant(request.POST)
        #check if the form is valid:
        if form.is_valid():
            #save it to the database
            form.save()
            return redirect("char-list")
    #handle the GET request(user entering the site):
    else:
        form = Summon_Servant()
        #render it inside char_list so user can see it their:
        return render(request,"logbook/char_list.html",{"form":form})
#create a function for the base html:
def home(request):
    #when the user enters the site this is what they see first:
    context = {"title":"Hi welcome to my fgo character list choose your favorit character:",
    #make it so the views also render the searchbar
"form":Summon_Servant()}
    return render(request,"logbook/base.html",context)

#create a list of  the fgo characters from the database:
def char_list(request):
#get all the character field from the database:
    char = Fgo.objects.all()
    #store them inside a context dictionary:
    context = {"char":char,"form":Summon_Servant()}
    #return the dictionary and render to html:
    return render(request,"logbook/char_list.html",context)

#create a servant detail logic:
def detail_page(request,pk):
    #make it so if a servant is clicked they get redirected to a detailed page:
    #(gets the pk for the  servant we want:)
    get_servant(chosen_servant.name)
    #store it in a context dictionary:
    context = {"get_servant":get_servant}
    return render(request,"logbook/servant_detail.html",context)




    
