from django.urls import path
from .views import *

urlpatterns = [
    path('notes',note_list),
    path('note/create/',note_create),
    path('note/<id>/edit',note_edit)
]