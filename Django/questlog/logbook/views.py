#2 this is where i display the actual data on a webpage
from django.shortcuts import render #helper to render templates
from .models import Quest, Servant,Construct #imports our data model
from .forms import QuestForm
from django.shortcuts import redirect#lets me redirct user to a page
# Create a view to display all quests
def quest_list(request):
    quests = Quest.objects.all()#Get all Quest objects from database
    context = {"quests":quests} #Create a dictionary to pass data to the template
    return render(request,"logbook/quest_list.html",context)

#A view to display all servantes
def servant_list(request):
        servants = Servant.objects.all()  # Get all Servant objects from the database
        context = {"servants": servants} # create a dictionary to pass data to the template
        return render(request, "logbook/servant_list.html",context)#render the template with the data

# create a view for my construct so my html can render it
def construct_list(request):
    constructs = Construct.objects.all()#gets all the construct objects
    #creat a dictionary so you can loop over it in html
    context = {"constructs":constructs}
    #return the reqeust,where the view will go,the info its sending
    return render(request,"logbook/construct_list.html",context)#q:why do we put them in ""?

#create a default hompage:
def home(request):
    context = {}
    return render(request,"logbook/base.html",context)

#create a view function for my form
def create_quest(request):
    if request.method == "POST":#checks if the user sent a GET request(submits data)
        form = QuestForm(request.POST)# gives the class the posted request
        if form.is_valid():#checks if my expresion is valid
            form.save()#adds the form into my Quest database
            return redirect("quest-list")#redirects the user to the page
    else:
        form = QuestForm()#sends a GET request and displays an empty form for the user to input data

    context = {"form": form}
    return render(request,"logbook/create_quest.html", context)

def quest_detail(request,pk):
    chosen_quest = Quest.objects.get(pk=pk)#grabs the unique id of the chosen quest
    context ={"chosen_quest":chosen_quest}
    return render(request,"logbook/quest_detail.html",context)








