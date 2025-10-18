# Import Django's model system to define database tables
from django.db import models

# Define a model to represent FGO servants
class Fgo(models.Model):
    # Character name — globally unique so it can’t be created twice
    name = models.CharField(max_length=50, unique=True)

    # Noble Phantasm name (special move)
    np = models.CharField(max_length=45, blank=True)#lets me keep the field blank

    # Class name (e.g., Saber, Archer, etc.)
    class_name = models.CharField(max_length=12, blank=True)

    # Image URL or file path (simple text field for now)
    image = models.CharField(max_length=255, blank=True)

    # String representation of the object — how it shows up in admin or print()
    def __str__(self):
        return self.name
