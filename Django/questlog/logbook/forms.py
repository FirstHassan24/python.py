#lets me make a form for my models(dont have to use admin)
from django import forms
from .models import Quest,Servant

# This class defines the structure of the form used to create a new Quest.
# It's a ModelForm, which means Django will automatically build the form fields
# based on the fields defined in the Quest model.
class QuestForm(forms.ModelForm):
    # The 'Meta' class tells the ModelForm which model it should be based on
    # and which fields from that model should be included in the form.
    class Meta:
        # Specify that this form is for the 'Quest' model.
        model = Quest
        # Include all fields from the Quest model in the form.
        fields = '__all__'

#defines the structure needed to make a new servant
class ServantForm(forms.ModelForm):
    class Meta:
        #specify this form is for servants
        model = Servant
        #includes all the field from servant model
        fields = ['name']
