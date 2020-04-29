from django import ModelForm, forms

class JournalForm(forms.Form):
    journal_name = forms.CharField(label='Journal Name', max_length=256)
