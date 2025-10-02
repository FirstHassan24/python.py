from django.db import models

# Create your models here.

# This model defines the structure for a single Monster Hunter Quest.
# Each instance of this class will be a single row in the 'logbook_quest' table in our database.
class Quest(models.Model):  # Inherits from Django's Model class
    # A field for the quest's title, stored as a string with a max length of 100 characters.
    title = models.CharField(max_length=100)
    # A field for the quest's rank (e.g., "Low Rank", "High Rank"), stored as a string.
    rank = models.CharField(max_length=10)
    # A field for the name of the monster to be hunted.
    target_monster = models.CharField(max_length=100)
    # A field for the reward amount, stored as a positive integer.
    reward_zenny = models.PositiveIntegerField()
    # A timestamp that is automatically set to the current date and time only when the quest is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This special method defines how a Quest object should be represented as a string.
    # It's used in the Django admin site and in the shell for easy identification.
    def __str__(self):
        return f"{self.title} ({self.rank})"

# This model defines the structure for a single Fate/Grand Order Servant.
class Servant(models.Model):
    # A field for the Servant's name.
    name = models.CharField(max_length=100)
    # A field for the Servant's class (e.g., Saber, Archer, Lancer).
    class_type = models.CharField(max_length=20)
    # A field for the Servant's star rarity (1-5).
    rarity = models.PositiveSmallIntegerField()
    # A field for the Servant's Noble Phantasm name.
    np_name = models.CharField(max_length=100)
    # A timestamp that is automatically set when the Servant is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This defines how a Servant object should be represented as a string.
    def __str__(self):
        return f"{self.name} ({self.class_type})"

# This model defines the structure for a single Punishing: Gray Raven Construct.
class Construct(models.Model):
    # A field for the Construct's name (e.g., "Lucia: Plume").
    name = models.CharField(max_length=100)
    # A field for the Construct's elemental damage type (e.g., "Ice", "Fire").
    element = models.CharField(max_length=30)
    # A field for the Construct's role in a team (e.g., "Attacker", "Tank").
    role = models.CharField(max_length=20)
    # A timestamp that is automatically set when the Construct is first created.
    created_at = models.DateTimeField(auto_now_add=True)

    # This defines how a Construct object should be represented as a string.
    def __str__(self):
        return f"{self.name} ({self.element})"

