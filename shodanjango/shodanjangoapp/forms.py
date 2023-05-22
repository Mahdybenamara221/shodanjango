from django import forms
from shodanjangoapp.models import information,address
class form(forms.ModelForm):
    class Meta:
        model=information
        fields="__all__"

class form2(forms.ModelForm):
    class Meta:
        model=address
        fields="__all__"