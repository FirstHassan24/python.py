from django.db import models  # Import Django model base classes

# Create your models here.
class Quest(models.Model):  # Define the Quest table/schema
    title = models.CharField(max_length=100)  # Short quest title text
    rank = models.CharField(max_length=10)  # Quest rank, e.g., LR/HR/MR
    target_monster = models.CharField(max_length=100)  # Target monster name
    reward_zenny = models.PositiveIntegerField()  # Reward amount in zenny (non-negative)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp set at creation

    def __str__(self):  # Human-readable representation (admin/shell)
        return f"{self.title} ({self.rank})"  # What to display for a Quest


class Servant(models.Model):  # Define the FGO Servant table/schema
    name = models.CharField(max_length=100)  # Servant name
    class_type = models.CharField(max_length=20)  # Class: Saber/Archer/Lancer/etc.
    rarity = models.PositiveSmallIntegerField()  # Star rarity 1–5 (non-negative small int)
    np_name = models.CharField(max_length=100)  # Noble Phantasm name
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp set at creation

    def __str__(self):  # Human-readable representation (admin/shell)
        return f"{self.name} [{self.class_type}] ★{self.rarity}"  # Display name + class + stars
    
#create a construct blueprint
class Construct(models.Model):
#what are the 3 things every construct needs:
    name = models.CharField(max_length=100)
    element = models.CharField(max_length =30)
    roll = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}, {self.element}, {self.roll}"
#dont forget to migrate after updating the model



