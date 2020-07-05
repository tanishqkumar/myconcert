from django.db import models
from datetime import date
from django import forms
from django.contrib.auth.models import User

JOURNAL_NAME_CHOICES = [
    ('NEJM', 'New England Journal of Medicine'),
    ('JVS', 'Journal of Vascular Surgery'),
]

MEMBERSHIP_NAME_CHOICES = [
    ('ACS', 'American College of Surgeons'),
    ('AMA', 'American Medical Association'),
]

CREDIT_FOR_CHOICES = [
    ('ABS', 'American Board of Surgery'),
    ('ABMS', 'American Board of Medical Specialties'),
]

BOARDSTATE_CREDITS = {
    'ABS': 30,
    'AMBS': 25,
    'NBPAS': 20,
    'NY': 5, 
}

# Create your models here.
class JournalEntry(models.Model):
    name = models.CharField(
        null=False,
        choices=JOURNAL_NAME_CHOICES,
        max_length=256,
        )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="journals",
        null=True,
        )

    renewal_date = models.DateField(
        verbose_name="Date of Renewal", 
        auto_now=False, 
        auto_now_add=False, 
        blank=True,
        null=True,
        )

    cme_available = models.DateField(
        verbose_name="CME Available", 
        auto_now=False, 
        auto_now_add=False, 
        blank=True,
        null=True,
        )

    sub_cost = models.FloatField(
        blank=True, 
        null=False, 
        max_length=6, 
        verbose_name='Subscription Cost',
        )

    icon_link = models.CharField(
        null=True, 
        max_length=1024, 
        blank=True)

    credit_for = models.CharField(
        null=True,
        choices=CREDIT_FOR_CHOICES,
        max_length=256)
    
    def __str__(self):
        return self.name

class MembershipEntry(models.Model):
    name = models.CharField(
        null=False,
        choices=MEMBERSHIP_NAME_CHOICES,
        max_length=256,
        )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="memberships",
        null=True,
    )

    renewal_date = models.DateField(
        verbose_name="Date of Renewal",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )

    cme_available = models.DateField(
        verbose_name="CME Available",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )

    sub_cost = models.FloatField(
        blank=True,
        null=True,
        max_length=6,
        verbose_name="Subscription Cost",
    )

    icon_link = models.CharField(
        null=True,
        max_length=1024,
        blank=True)

    credit_for = models.CharField(
        null=True,
        choices=CREDIT_FOR_CHOICES,
        max_length=256)

    def __str__(self): return self.name

class boardEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="boards",
        null=True,
    )

    name = models.CharField(
        null=True,
        max_length=1024,
        )

    num_cme_credits = models.IntegerField(default=10)

    def __str__(self): return self.name
