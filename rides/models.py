from django.db import models


class Person(models.Model):
    """Ride-share registrant. Address is stored but not shown in search results."""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=128, blank=True)

    # Origination: full address stored for DB; origin city/state used for search and display (no address shown)
    origination = models.CharField(max_length=128, help_text="Full origination address (stored, not displayed in search)")
    origination_state = models.CharField(max_length=2, blank=True)
    origin_city = models.CharField(max_length=64, blank=True)

    destination_city = models.CharField(max_length=64)
    destination_state = models.CharField(max_length=2)
    date = models.DateField()
    time = models.TimeField()
    taking_passengers = models.BooleanField(default=False)
    seats_available = models.IntegerField(default=0)
