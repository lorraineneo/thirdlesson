from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Note

# Create your views here.
def notes_list(request):
    allnotes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': allnotes})   
    
def note(request, note_id):
    note = Note.objects.get(id=note_id)
    responsetext = ""
    responsetext += "<h1>" + str(note.id) + "</h1>"
    responsetext += "<h2>" + note.title + "</h2>"
    responsetext += "<h2>" + note.content + "</h2>"
    return HttpResponse(responsetext)