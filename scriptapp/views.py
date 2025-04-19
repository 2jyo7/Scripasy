from django.shortcuts import render, redirect , get_object_or_404
from .models import Chapter, ScriptEntry
from .forms import ScriptEntryForm

def script_input(request):
    # Load entries from session (empty list if none)
    entries = request.session.get('entries', [])
    print(request)
    if request.method == 'POST':
        if 'add' in request.POST:
            # Add a new entry to the session
            entry = {
                'place': request.POST.get('place'),
                'emotion': request.POST.get('emotion'),
                'voice': request.POST.get('voice'),
                'context': request.POST.get('context'),
            }

            # Prevent empty entries
            if any(entry.values()):
                entries.append(entry)
                request.session['entries'] = entries
            return render(request, 'scriptapp/script_input.html', {'entries': entries})

        elif 'publish' in request.POST:
            chapter_title = request.POST.get('chapter_title')

            # Save to DB only if title and entries exist
            if chapter_title and entries:
                chapter = Chapter.objects.create(title=chapter_title)

                for entry in entries:
                    ScriptEntry.objects.create(
                        chapter=chapter,
                        place=entry.get('place', ''),
                        emotion=entry.get('emotion', ''),
                        voice=entry.get('voice', ''),
                        context=entry.get('context', '')
                    )

                # Clear session after saving
                request.session['entries'] = []
                return redirect('chapter_list')

    return render(request, 'scriptapp/script_input.html', {'entries': entries})


def chapter_list(request):
    chapters = Chapter.objects.prefetch_related('entries').all()
    return render(request, 'scriptapp/chapter_list.html', {'chapters': chapters})


def edit_entry(request, entry_id):
    entry = get_object_or_404(ScriptEntry, id=entry_id)
    if request.method == 'POST':
        form = ScriptEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('chapter_list')
    else:
        form = ScriptEntryForm(instance=entry)
    return render(request, 'scriptapp/edit_entry.html', {'form': form})

def delete_entry(request, entry_id):
    entry = get_object_or_404(ScriptEntry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('chapter_list')
    return render(request, 'scriptapp/confirm_delete.html', {'entry': entry})