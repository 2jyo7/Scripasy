from django import forms
from .models import ScriptEntry

class ScriptEntryForm(forms.ModelForm):
    class Meta:
        model = ScriptEntry
        fields = [ 'place', 'emotion', 'voice', 'context']
        widget = {
            'context': forms.Textarea(attrs={'rows': 4}),
        }
