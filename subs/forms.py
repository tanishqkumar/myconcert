from django import forms
from .models import JournalEntry, MembershipEntry

class JournalEntryForm(forms.ModelForm):
    """Form definition for JournalEntry."""

    class Meta:
        """Meta definition for JournalEntryform."""

        model = JournalEntry
        fields = ('name', 'renewal_date', 'sub_cost')

class MembershipEntryForm(forms.ModelForm):
    """Form definition for MembershipEntry."""

    class Meta:
        """Meta definition for MembershipEntryform."""

        model = MembershipEntry
        fields = ('name', 'renewal_date', 'sub_cost')

