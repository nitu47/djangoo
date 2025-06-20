from django.contrib import admin
from .models import Note

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','description','date']
    list_filter = ['title']
    search_fields = ['title']
    list_editable = ['description',]
    list_per_page = 2
    

