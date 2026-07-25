from django import forms
from .models import Aktivitas

class AktivitasForm(forms.ModelForm):
    class Meta:
        model = Aktivitas
        fields = ['date_ohin', 'oras_hahu', 'oras_hotu', 'atividade', 'deskrisaun']
        labels = {
            'date_ohin': 'Date',
            'oras_hahu': 'Start Time',
            'oras_hotu': 'End Time',
            'atividade': 'Activity',
            'deskrisaun': 'Description',
        }
        widgets = {
            'date_ohin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'oras_hahu': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'oras_hotu': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'atividade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activity title'}),
            'deskrisaun': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Detailed description...'}),
        }
