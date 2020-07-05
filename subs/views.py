from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import MembershipEntryForm, JournalEntryForm, UserSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import random

# Create your views here.
@login_required()
def chart(request):
    # ABS: 30, where ABS is label and 30 is data
    user_boardstate_entries = boardEntry.objects.filter(user=request.user)
    return JsonResponse(data={
        'labels': [e.name for e in user_boardstate_entries],
        'data': [e.num_cme_credits for e in user_boardstate_entries],
    })

@login_required()
def boardstate(request): 
    context = {}
    context['dict'] = BOARDSTATE_CREDITS
    if request.method == 'POST':
        # take posted board name as dropdown option
        name = request.POST.get('name')
        creds = BOARDSTATE_CREDITS[name]
        # generate randint to go with that entry
        e = boardEntry(name=name, num_cme_credits=creds, user=request.user)
        e.save()
        # post back all the entries, incl. the new one, so they can be the instance of the form
        context['board_entries'] = boardEntry.objects.all()
        if len(boardEntry.objects.all()) == 0:
            context['is_graph'] = False
        else:
            context['is_graph'] = True
        return render(request, 'board.html', context)
    else: 
        context['board_entries'] = boardEntry.objects.all()
        if len(boardEntry.objects.all()) == 0:
            context['is_graph'] = False
        else:     
            context['is_graph'] = True
        return render(request, 'board.html', context)
    return render(request, 'state.html')



@login_required
def subsmems(request):
    user_journal_entries = JournalEntry.objects.filter(user__username=request.user.username)
    user_membership_entries = MembershipEntry.objects.filter(user__username=request.user.username)

    context = {
        'user_journal_entries': user_journal_entries,
        'user_membership_entries': user_membership_entries,
        'current_user_name': request.user.username,
        'journal_form': JournalEntryForm(),
        'membership_form': MembershipEntryForm(),
    }
    if request.method == 'POST':
        # if request was submitted using journalForm buttom
        if 'journalForm' in request.POST:
            # create, check, process data from form, redirect
            context['journal_form'] = JournalEntryForm(request.POST)
            if context['journal_form'].is_valid:
                journalEntry = context['journal_form'].save(commit=False)
                journalEntry.user = request.user
                journalEntry.save()
                return render(request, 'subsmems.html', context) 
        # if request was submitted using memberForm button
        elif 'membershipForm' in request.POST:
            # create, check, process data from form, redirect
            context['membership_form'] = MembershipEntryForm(request.POST)
            if context['membership_form'].is_valid:
                membershipEntry = context['membership_form'].save(commit=False)
                membershipEntry.user = request.user
                membershipEntry.save()
                return render(request, 'subsmems.html', context)

    elif request.method == 'GET':
        return render(request, 'subsmems.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('subsmems')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def deleteJournalEntry(request):
    entry_to_delete = JournalEntry.objects.filter(
        pk=request.POST.get('id'))
    entry_to_delete.delete()    
    return redirect('subsmems')


@login_required
def deleteMembershipEntry(request):
    entry_to_delete = MembershipEntry.objects.filter(
        pk=request.POST.get('id'))
    entry_to_delete.delete()
    return redirect('subsmems')


@login_required
def tablepage(request):
    return render(request, 'tablepage.html') 
