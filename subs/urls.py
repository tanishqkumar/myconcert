from .forms import UserLoginForm
from django.urls import path, include
from django.contrib.auth import views
from .views import subsmems, signup, deleteJournalEntry, deleteMembershipEntry

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
    path('deleteMembershipEntry', deleteMembershipEntry, name='deleteMembershipEntry')
]



