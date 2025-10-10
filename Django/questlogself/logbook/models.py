from django.db import models

# Create your models here.
#create a model for fgo characters 
class Fgo(models.Model):
    name = models.CharField(max_length=50)
    np = models.CharField(max_length=45)
    clas = models.CharField(max_length=12)
    #show the name of the character made:
    def __str__(self):
        #returns the characters name:
        return self.name


