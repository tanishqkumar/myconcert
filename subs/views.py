from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import JournalEntry, MembershipEntry, JOURNAL_NAME_CHOICES, MEMBERSHIP_NAME_CHOICES
from .forms import JournalEntryForm, MembershipEntryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def subsmems(request):
    user_journal_entries = JournalEntry.objects.filter(user__username=request.user.username)
    # all_membership_entries = MembershipEntry.objects.all()
    form = JournalEntryForm()
    context = {
        'user_journal_entries': user_journal_entries,
        'current_user_name': request.user.username,
        # 'all_membership_entries': all_membership_entries,
        'form': form,
    }
    if request.method == 'POST':
        # create, check, process data from form, redirect
        context['form'] = JournalEntryForm(request.POST)
        if context['form'].is_valid:
            journalEntry = context['form'].save(commit=False)
            journalEntry.user = request.user
            journalEntry.save()
            return render(request, 'subsmems.html', context) 

    else:
        return render(request, 'subsmems.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('subsmems')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
