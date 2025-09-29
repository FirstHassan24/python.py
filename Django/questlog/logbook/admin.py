from django.contrib import admin   # Import the admin site functionality


# Register your models here.
from .models import Quest, Servant, Construct  # Import your Quest and Servant models

admin.site.register(Quest)  # Make the Quest model available in the admin site
admin.site.register(Servant)  # Make the Servant model available in the admin site
admin.site.register(Construct)