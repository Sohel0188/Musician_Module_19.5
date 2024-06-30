from django import forms
from .models import Album
from musician.models import Musician

class AlbumForm(forms.ModelForm):
    
    rerelease_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'id': 'required'}))
    class Meta:
        model = Album
        fields = '__all__'