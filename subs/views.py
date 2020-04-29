from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import JournalEntry, MembershipEntry, JOURNAL_NAME_CHOICES, MEMBERSHIP_NAME_CHOICES, JournalEntryForm, MembershipEntryForm
# from .forms import JournalForm

# Create your views here.
def subsmems(request):
    all_journal_entries = JournalEntry.objects.all()
    # all_membership_entries = MembershipEntry.objects.all()
    # all_journal_names = [x[1] for x in JOURNAL_NAME_CHOICES]
    # all_membership_names = [x[1] for x in MEMBERSHIP_NAME_CHOICES]
    form = JournalEntryForm()
    context = {
        'all_journal_entries': all_journal_entries,
        # 'all_membership_entries': all_membership_entries,
        'form': form,
    }
    if request.method == 'POST':
        # create, check, process data from form, redirect
        context['form'] = JournalEntryForm(request.POST)
        if context['form'].is_valid:
            context['form'].save()
            return render(request, './subs/subsmems.html', context) 

    else:
        return render(request, './subs/subsmems.html', context)

