from django.urls import path

from .views import subsmems

urlpatterns = [
    path('', subsmems, name='subsmems'),
]
