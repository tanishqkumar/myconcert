from django.db import models
from datetime import date
from django import forms

JOURNAL_NAME_CHOICES = [
    ('New England Journal of Medicine', 'New England Journal of Medicine'),
    ('Journal of Vascular Surgery'),
]

MEMBERSHIP_NAME_CHOICES = [
    ('American College of Surgeons'),
    ('American Medical Association'),
]

CREDIT_FOR_CHOICES = [
    ('American Board of Surgery'),
    ('American Board of Medical Specialties'),
]

# Create your models here.
class JournalEntry(models.Model):
    name = models.CharField(
        null=False,
        choices=JOURNAL_NAME_CHOICES,
        max_length=256)

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

class JournalEntryForm(forms.ModelForm):
    """Form definition for JournalEntry."""

    class Meta:
        """Meta definition for JournalEntryform."""

        model = JournalEntry
        fields = ('name', 'renewal_date', 'sub_cost')


class MembershipEntry(models.Model):
    name = models.CharField(
        null=False,
        choices=MEMBERSHIP_NAME_CHOICES,
        max_length=256)

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


class MembershipEntryForm(forms.ModelForm):
    """Form definition for MembershipEntry."""

    class Meta:
        """Meta definition for MembershipEntryform."""

        model = MembershipEntry
        fields = ('name', 'renewal_date', 'sub_cost')
