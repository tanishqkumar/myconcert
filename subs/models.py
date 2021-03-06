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

# Create your models here.

class State(models.Model):

    name = models.CharField(
        null=True,
        max_length=1024,
    )

    cycle_length = models.IntegerField(
        null=True,
    )

    cycle_total_cme_req = models.IntegerField(
        null=True,
    )

    cycle_cat_1_req = models.IntegerField(
        null=True,
    )

    cycle_cat_2_req = models.IntegerField(
        null=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    def __str__(self): return self.name


class StateEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="state_entries",
    )

    state = models.ForeignKey(
        State,
        null=True,
        on_delete=models.CASCADE,
        related_name="users",
    )

    first_reg = models.DateField(
        null=True,
        auto_now=False,
        auto_now_add=False
    )

    last_reg = models.DateField(
        null=True,
        auto_now=False,
        auto_now_add=False
    )

    def __str__(self): return self.state.name

class Board(models.Model):

    name = models.CharField(
        null=True,
        max_length=1024,
    )

    cycle_1_length = models.IntegerField(
        null=True,
    )

    cycle_1_total_cme_req = models.IntegerField(
        null=True,
    )

    cycle_1_cat_1_req = models.IntegerField(
        null=True,
    )

    cycle_1_self_req = models.IntegerField(
        null=True,
    )

    cycle_1_cat_2_req = models.IntegerField(
        null=True,
    )

    cycle_2_length = models.IntegerField(
        null=True,
    )

    cycle_2_total_cme_req = models.IntegerField(
        null=True,
    )

    cycle_2_cat_1_req = models.IntegerField(
        null=True,
    )

    cycle_2_self_req = models.IntegerField(
        null=True,
    )

    cycle_2_cat_2_req = models.IntegerField(
        null=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    def __str__(self): return self.name



class BoardEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="board_entries",
    )

    board = models.ForeignKey(
        Board,
        null=True,
        on_delete=models.CASCADE,
        related_name="users",
        )

    first_reg = models.DateField(
        null=True,
         auto_now=False, 
         auto_now_add=False
    )

    last_reg = models.DateField(
        null=True,
         auto_now=False, 
         auto_now_add=False
    )

    timeline_tag = models.CharField(
        null=True,
        max_length=8
    )

    def __str__(self): 
        return self.board.name



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

