from django.db import models


class Personnel(models.Model):
    slot        = models.PositiveSmallIntegerField(unique=True)
    name        = models.CharField(max_length=120)
    color_class = models.CharField(max_length=10, default='u1')

    class Meta:
        ordering = ['slot']

    def __str__(self):
        return f"[{self.slot}] {self.name}"


class Incident(models.Model):
    time      = models.CharField(max_length=10)
    date      = models.DateField()
    location  = models.CharField(max_length=255)
    involved  = models.CharField(max_length=20)
    occupancy = models.CharField(max_length=120, blank=True, default='')
    damage    = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    injured   = models.PositiveIntegerField(default=0)
    casualty  = models.PositiveIntegerField(default=0)
    station   = models.CharField(max_length=60, blank=True, default='')
    engine    = models.CharField(max_length=60, blank=True, default='')
    alarm     = models.CharField(max_length=20, default='1st Alarm')
    inputter  = models.CharField(max_length=120)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.date} {self.time} — {self.location}"