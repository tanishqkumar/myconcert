from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import MembershipEntryForm, JournalEntryForm, UserSignupForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import random

# Create your views here.
@login_required()
@csrf_exempt 
def chart(request):
    # return list of lists, first list is row (eg ABS), and nested list is total, cat1, cat2, self as labels and corresponding split
    # from the board_dict is the list for data
    context = {}
    board_entries = BoardEntry.objects.filter(user=request.user)
    rows = {}
    row_labels, row_data = [], []
    for eo in board_entries:
        row_labels = ['cycle_1_total_cme_req', 'cycle_1_cat_1_req',
                      'cycle_1_self_req', 'cycle_1_cat_2_req']
        row_data = [eo.board.cycle_1_total_cme_req, eo.board.cycle_1_cat_1_req,
                    eo.board.cycle_1_self_req, eo.board.cycle_1_cat_2_req]
    print('row labels then data: ', row_labels, row_data)
    return JsonResponse(data={
        'labels': row_labels,
        'data': row_data,
    })

@login_required()
def del_board_entry(request):
    # ABS: 30, where ABS is label and 30 is data
    # take the entry name and cycle and we'll get the entry associated with that account
    BoardEntry.objects.filter(user=request.user, board__name=request.POST['entry_name']).delete()
    print('deleted', request.POST['entry_name'])
    return redirect('boardstate')

# get graph working with current setup
# modify schema to mimic excel sheet
# add a couple of items and get graph working
# write script to scrape excel sheet and get graph working in a basic way
# take in info about birth/grad date for user at beginning and use that to determine cycle and grad info
# test persistance and expand journal list for main page/connect to graph db
# rename url and go live

@login_required()
def boardstate(request): 
    context = {}
    context['BOARD_INFO'] = BOARD_INFO
    if request.method == 'POST':
        name = request.POST.get('name')
        board = Board.objects.get(name=name)
        e = BoardEntry(board=board, user=request.user)
        e.save()
        # post back all the entries, incl. the new one, so they can be the instance of the form
        board_entries = BoardEntry.objects.filter(user=request.user)
        context['user_board_entries'] = board_entries
        # construct dict with all board entries for this person, and then add k,v within each key
        # that represent the minor info by querying the board_info here on the backend
        if len(BoardEntry.objects.all()) == 0:
            context['is_graph'] = False
            # print('graph wont render')
        else:
            # context['is_graph'] = False
            context['is_graph'] = True
            # print('graph should render')
        return render(request, 'board.html', context)
    
    else: 
        print('get req')
        for x in BoardEntry.objects.all():
            print(x.board)
        board_entries = BoardEntry.objects.filter(user=request.user)
        context['board_entries_w_info'] = {}
        context['user_board_entries'] = board_entries
        if len(BoardEntry.objects.all()) == 0:
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
