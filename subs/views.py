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
from datetime import date, datetime
from .utils import *


# TODO
# special cme for state: just one time on first cycle depending on dates?
# remind me relevance of expiration dates
# re: annual tab can retrofit
# is None a board choice or a choice of date entry
    # don't make date entry compulsory if it's the latter
 
# Create your views here.
@login_required()
@csrf_exempt 
def chart(request):
    print('obj id is', request.POST['obj_id'])
    obj_id = request.POST['obj_id']
    context = {}
    board_entries, state_entries = BoardEntry.objects.filter(
        user=request.user), StateEntry.objects.filter(user=request.user)
    # check each obj id to see which type of obj and then return 2 lists accodingly for that type of object
    try: 
        eo = BoardEntry.objects.get(pk=obj_id)
        if eo.timeline_tag == '1':
            row_labels = ['Cat I',
                        'Self', 'Cat II']
            row_data = [eo.board.cycle_1_cat_1_req,
                        eo.board.cycle_1_self_req, eo.board.cycle_1_cat_2_req]
        else:
            row_labels = ['Cat I',
                        'Self', 'Cat II']
            row_data = [eo.board.cycle_2_cat_1_req,
                        eo.board.cycle_2_self_req, eo.board.cycle_2_cat_2_req]
    except:
        eo = StateEntry.objects.get(pk=obj_id)
        row_labels = ['Cat I', 'Cat II']
        row_data = [eo.state.cycle_cat_1_req, eo.state.cycle_cat_2_req]
    return JsonResponse(data={
        'labels': row_labels,
        'data': row_data,
    })

@login_required()
def del_board_entry(request):
    BoardEntry.objects.filter(user=request.user, board__name=request.POST['entry_name']).delete()
    print('deleted', request.POST['entry_name'])
    return redirect('boardstate')


@login_required()
def del_state_entry(request):
    StateEntry.objects.filter(user=request.user, state__name=request.POST['entry_name']).delete()
    print('deleted', request.POST['entry_name'])
    return redirect('boardstate')

# add date fields so user can pick f/l date info and store as part of entry
# use f/l to determine cycle credits output on graph
    # if first_reg for board is > board.cycle_1_length, set timeline_tag to 1, else 2
# create state object and populate as counterpoint to ABS
# implement b/s button st approppriate dropdown shown selectively
# add f/l etc func to the state template
# ensure each works fine individually
# try to add annual tab on graph for each
# add multiple graph func for multiple rows being added

@login_required()
def boardstate(request):
    context = {}
    context['board_info'] = Board.objects.all()
    context['state_info'] = State.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        first_reg = datetime.strptime(
            request.POST['first_reg'], '%Y-%m-%d').date()
        last_reg = datetime.strptime(
            request.POST['last_reg'], '%Y-%m-%d').date()
        try:
            board = Board.objects.get(name=name)
            print('board shit')
            b = BoardEntry(board=board, user=request.user,
                           first_reg=first_reg, last_reg=last_reg)
            b.save()
            AssignBoardTimelineTags(request, b, first_reg)
        except:
            state = State.objects.get(name=name)
            print('state shit')
            s = StateEntry(state=state, user=request.user,
                           first_reg=first_reg, last_reg=last_reg)
            s.save()
            print('all state entries are', StateEntry.objects.all())
    board_entries, state_entries = BoardEntry.objects.filter(
        user=request.user), StateEntry.objects.filter(user=request.user)
    context['user_board_entries'], context['user_state_entries'] = board_entries, state_entries
    context['all_user_entries'] = list(board_entries) + list(state_entries)
    # send a combined list for board and state in the order they appear
    # so that you can create many graphs by iterating over that list
    if len(board_entries) == 0 and len(state_entries) == 0:
        context['is_graph'] = False
    else:
        context['is_graph'] = True
    return render(request, 'board.html', context)



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
