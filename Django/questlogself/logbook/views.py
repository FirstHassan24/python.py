from django.shortcuts import render
from .models import Fgo

# Create your views here.
#create a list of  the fgo characters from the database:
def char_list(request):
#get all the characters from the database:
    char = Fgo.objects.all
    #store them inside a context dictionary:
    context = {"char":char}
    #return the dictionary and render to html:
    return render(request,"logbook/char_list.html",context)


    
