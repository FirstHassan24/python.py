#import forms so django knows what your trying to do:
from django import forms 
#import the Servants model so we can use it to summon servants
from .models import Servant

class ServantForm(forms.ModelForm):
    class Meta:
        model = Servant
        fields = ["name","class_name","rarity","np_name"] 