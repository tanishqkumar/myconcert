from .forms import UserLoginForm
from django.urls import path, include
from django.contrib.auth import views
from .views import *

urlpatterns = [
    path('', subsmems, name='subsmems'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', signup, name='signup'), 
    path(
        'login/',
        views.LoginView.as_view(
            authentication_form=UserLoginForm,
        ),
        name='login'
    ), 
    path('deleteJournalEntry', deleteJournalEntry, name='deleteJournalEntry'),
    path('deleteMembershipEntry', deleteMembershipEntry, name='deleteMembershipEntry'), 
    path('table', tablepage, name='tablepage'), 
    path('boardstate', boardstate, name='boardstate'), 
    path('chart', chart, name='chart'), 
    path('del_board_entry', del_board_entry, name='del_board_entry'), 
]



