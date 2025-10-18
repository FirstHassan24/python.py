from django.shortcuts import render, redirect, get_object_or_404
from .models import Fgo
# Import error handler for when database rules are violated (e.g., duplicate name)
from django.db import IntegrityError
# Import the servant form the user fills out
from .forms import Summon_Servant
from django.http import HttpResponse
# Import the services module for API functions
from .services import get_servant

# Create your views here.
# Handle the form submission to create a new servant
def summon(request):
    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Bind the submitted data to the form
        form = Summon_Servant(request.POST)

        # Check if all form data passes validation
        if form.is_valid():
            # Try saving the form — database is the final authority
            try:
                # Save the new servant to the database
                form.save()

                # Redirect the user back to the character list page
                return redirect("char-list")

            # Catch any duplicate errors that slip past validation
            except IntegrityError:
                # Attach a friendly error to the form instead of crashing
                form.add_error("name", "This servant already exists.")

        # If the form isn’t valid, it’ll fall through and re-render with errors
    else:
        # For GET requests (when visiting the page), show an empty form
        form = Summon_Servant()
        print(form.errors)

    # Render the form on the character list page, including any validation errors
    return render(request, "logbook/char_list.html", {"form": form})

# Function to render the home page
def home(request):
    # Define the context for the home page
    context = {
        # Title to display on the home page
        "title": "Hi welcome to my fgo character list choose your favorit character:",
        # Form for summoning servants
        "form": Summon_Servant()
    }
    # Render the base template with the context
    return render(request, "logbook/base.html", context)

# Function to list all FGO characters
def char_list(request):
    # Retrieve all Fgo objects from the database
    char = Fgo.objects.all()
    # Store the characters and form in a context dictionary
    context = {
        # List of all characters
        "char": char,
        # Form for summoning servants
        "form": Summon_Servant()
    }
    # Render the char_list template with the context
    return render(request, "logbook/char_list.html", context)

# Function to display details of a specific servant
def detail_page(request, pk):
    # Get the servant object by primary key or return 404 if not found
    servant = Fgo.objects.get(pk=pk)
    # Extract the servant's name for API lookup
    servant_name = servant.name
    # Call the API function to get servant details
    api_data = get_servant(servant_name)
    # Store the API data in a context dictionary
    context = {
        # API data for the servant
        "api_data": api_data
    }
    # Render the servant_detail template with the context
    return render(request, "logbook/servant_detail.html", context)

# Function to delete a specific servant
def delete_servant(request, pk):
    # Get the servant object by primary key or return 404 if not found
    servant = get_object_or_404(Fgo, pk=pk)
    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # Delete the servant from the database
        servant.delete()
        # Redirect to the character list page after deletion
        return redirect("char-list")