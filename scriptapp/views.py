from django.shortcuts import render, redirect
from .forms import ScriptEntryForm
from .models import ScriptEntry, Chapter

def script_input_view(request):
    form = ScriptEntryForm()
    session_entries = request.session.get('entries', [])

    if request.method == 'POST':
        form = ScriptEntryForm(request.POST)
        if form.is_valid():
            entry_data = form.cleaned_data

            if 'add' in request.POST:
                # Add to session
                session_entries.append(entry_data)
                request.session['entries'] = session_entries
                return redirect('script_input')  # reload the form

            elif 'publish' in request.POST:
                # Create a new Chapter
                chapter = Chapter.objects.create(title="Untitled Chapter")

                # Save each entry into DB linked to this Chapter
                for data in session_entries:
                    ScriptEntry.objects.create(
                        chapter=chapter,
                        place=data['place'],
                        emotion=data['emotion'],
                        voice=data['voice'],
                        context=data['context']
                    )

                # Clear session
                request.session['entries'] = []
                return redirect('script_input')

    return render(request, 'scriptapp/script_input.html', {
        'form': form,
        'entries': session_entries,
    })
