# We need render for templates, redirect after save, and a helper to fetch by id or 404
from django.shortcuts import render,redirect,get_object_or_404
#our database model:
from .models import Servant
#our modelForm that matches servant fields:
from .forms import ServantForm

# Create your views here.
#create a list of servants:
def servant_list(request):
    #store all the servants in a variable:
    servants = Servant.objects.all
    return render(request,"logbook/servant_list.html",{"servant":servants})

# This view handles both displaying and processing the "Summon Servant" form
def servant_create(request):
    # If the user just clicked "Summon" (submitted the form)
    if request.method == "POST":
        # Fill the form with the data the user typed in
        form = ServantForm(request.POST)
        # Check if all fields are valid (non-empty, correct types, etc.)
        if form.is_valid():
            # Save the servant to the database (our local Chaldea records)
            form.save()
            # After summoning, send the user back to the list page
            return redirect("servant-list")
    # If the user is just visiting the page (GET request)
    else:
        # Create an empty form so the user can fill it out
        form = ServantForm()

    # Render the page using our form template and pass the form to it
    return render(request, "logbook/servant_form.html", {"form": form})

#This view handles existing servants:
def servant_update(request,pk):
    #find servant by its pk or show 404 not found"
    servant = get_object_or_404(Servant,pk)
    #if the user submited the form:
    if request.method == "POST":
        #bind the form to the posted data and the existing instance(so we update not create):
        form = ServantForm(request.POST, instance=servant)
        #validate the user input(types,required fields,unique name):
        form.is_valid()
        #save changes to the same row in the database:
        form.save
        #go back to the list after a successful update:
        return redirect("servant-list")
    else:
        # if its a get request show the form prefilled with the servants current data:
        form = ServantForm(instance=servant)
        #Render the same form template; pass a flag so we can change button text to “Update”:
        return render(request,"logbook/servant_form.html",{"form":form, "is_edit":True})
            