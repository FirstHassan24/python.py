from django import forms
from .models import Fgo
#let user  summon servants here:
class Summon_Servant(forms.ModelForm):
    #inherite the name field from models to here:
    class Meta:
        #tell it which database model to work with:
        model = Fgo
        #specify which field to use:
        fields =["name"]

    
        