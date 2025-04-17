from django.shortcuts import render, redirect
from .models import Chapter, ScriptEntry

def script_input(request):
    # Load entries from session (empty list if none)
    entries = request.session.get('entries', [])

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
