from django import forms
#let user  summon servants here:
class Summon_Servant(forms.ModelForm):
    #inherite the name field from models to here:
    class Meta:
        fields =["name"]

    
        