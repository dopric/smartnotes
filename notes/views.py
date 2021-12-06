from django.shortcuts import render
from .models import Note

def index(request):
    return render(request, 'notes/index.html', {'notes': Note.objects.all()})

