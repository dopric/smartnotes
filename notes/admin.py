from django.contrib import admin

# Register your models here.

from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
