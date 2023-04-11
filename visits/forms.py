from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('employee', 'date', 'time_visit_start', 'time_visit_end', 'reason')
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
            'time_visit_start': forms.TimeInput(attrs={'type': 'time'}),
            'time_visit_end': forms.TimeInput(attrs={'type': 'time'}),
            'reason': forms.TextInput(attrs={'class': 'form-control'})
        }
