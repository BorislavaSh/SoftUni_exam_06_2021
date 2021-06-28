from django.shortcuts import render, redirect

from notes.core.utils import get_profile
from notes.Notes_app.forms import DeleteNoteForm, NoteForm
from notes.Notes_app.models import Note


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create_profile')

    notes = Note.objects.all()

    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteNoteForm(instance=note)
        return render(request, 'note-delete.html', {'form': form})
    note.delete()
    return redirect('home')


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }

    return render(request, 'note-details.html', context)