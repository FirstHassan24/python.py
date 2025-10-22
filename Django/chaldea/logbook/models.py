from django.db import models

# Create your models here.
from django.db import models
class Servant(models.Model):
    #every servants name must be unique:
    name = models.CharField(max_length = 100, unique=True)
    #get the class names
    class_name = models.CharField(max_length=50,null=True,blank=True)
    #get the rarity of the servant:
    rarity = models.IntegerField(null=True, blank=True)
    #get the np name of the servant:
    np_name = models.CharField(max_length=100,null=True, blank=True)
   
    #make django show the name of the servant when printing:
    def __str__(self):
        return self.name