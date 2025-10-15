# Import Django’s form tools
from django import forms

# Import the Fgo model to build a form from it
from .models import Fgo

# Create a form class for adding new servants
class Summon_Servant(forms.ModelForm):
    # Define which model and fields this form is based on
    class Meta:
        model = Fgo
        fields = ["name", "np", "class_name", "image"]

    # Custom validation to prevent duplicates (case-insensitive)
    def clean_name(self):
        # Get the submitted name from the form data
        name = self.cleaned_data["name"]

        # Check if a servant with the same name already exists in the DB
        if Fgo.objects.filter(name__iexact=name).exists():
            # Raise a form-level error instead of crashing
            raise forms.ValidationError("This servant already exists.")

        # If no duplicates are found, return the valid name
        return name
