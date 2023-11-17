from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Notes

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # template_name = "notes/notes_list.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(DetailView):  # return note by pk
    model = Notes                   # the template has to be called notes_detail
    context_object_name = "note"    # what apears in the template
    # template_name = "notes/notes_list.html"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist!")
#     return render(request, 'notes/notes_detail.html', {'note': note})
