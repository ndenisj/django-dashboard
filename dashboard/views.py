from django.shortcuts import render, redirect
from notepad.forms import NoteModelForm
from notepad.models import Note


def home(request):
    notes = Note.objects.all(user=request.user)
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/notes/list')
    context = {
        'form': form,
        'object_list': notes,
    }

    return render(request, 'notepad/list.html', context)