from django.shortcuts import render, redirect
from .forms import NoteModelForm
from .models import Note

# Create your views here.
def create_view(request):
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/notes/list')

    context = {
        'form': form
    }

    return render(request, 'notepad/create.html', context)

def list_view(request):
    notes = Note.objects.all()

    context = {
        'object_list': notes
    }

    return render(request, 'notepad/list.html', context)