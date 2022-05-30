from uuid import uuid4

from django.db import models


class Event(models.Model):
    EVENT_TOPOLOGY_CHOICES = (
        ("V", "Virtual"),
        ("P", "Public"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    event_topology = models.CharField(max_length=1, choices=EVENT_TOPOLOGY_CHOICES)

    def __str__(self):
        return self.name


class Atendee(models.Model):
    SALUTATION_CHOICES = (
        ("MR", "Mr."),
        ("MRS", "Mrs."),
        ("MISS", "Miss."),
        ("MS", "Ms."),
    )
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    salutation = models.CharField(max_length=4, choices=SALUTATION_CHOICES)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    events = models.ManyToManyField("Event", db_index=True)

    def __str__(self):
        return f"{self.salutation} {self.first_name} {self.last_name}"
