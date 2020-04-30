from django.urls import path, include

from .views import subsmems, signup

urlpatterns = [
    path('', subsmems, name='subsmems'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', signup, name='signup')
]
