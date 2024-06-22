from django import forms
from app.models import moni
class monii(forms.ModelForm):
    class Meta:
        model=moni
        fields="__all__"