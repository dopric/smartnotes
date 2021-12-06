from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name="notes_index"),
    path('<int:pk>', views.NoteView.as_view())
]
