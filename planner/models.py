from django.db import models
from django.db.models import Sum

# Create your models here.

STATUS_CHOICES = (
    ('1', 'To invite'),
    ('2', 'Invited'),
    ('3', 'Confirmed'),
    ('4', 'Waiting'),
    ('5', 'Not Coming'),
    )


class Guests(models.Model):
    invited_family = models.CharField(max_length=100, primary_key=True)
    adults = models.IntegerField()
    children = models.IntegerField()
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='1')


    def __str__(self):
        return self.invited_family


class Finance(models.Model):
    item = models.CharField(max_length=100, primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class Buffet(models.Model):
    adult_price = models.DecimalField(max_digits=5, decimal_places=2)
    kid_price = models.DecimalField(max_digits=5, decimal_places=2)


