from django.http import Http404
from django.shortcuts import render
from .models import Note
from django.views.generic import ListView, DetailView


class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/index.html"

# def index(request):
#     return render(request, 'notes/index.html', {'notes': Note.objects.all()})


class NoteView(DetailView):
    model = Note
    context_object_name = "note"

# def note_details(request, note_id):
#     try:
#         note = Note.objects.get(id=note_id)
#         return render(request, 'notes/note_detail.html', {'note': note})
#     except Note.DoesNotExist:
#         return Http404()
