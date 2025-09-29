#lets me make a form for my models(dont have to use admin)
from django import forms
from .models import Quest,Servant,Construct#imports the models

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest # tells the form which model to build from
        fields = "__all__" # tells the form to include all fields from the model
