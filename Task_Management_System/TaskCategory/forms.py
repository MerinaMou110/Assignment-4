from django import forms
from . models import category

class ctegoryForm(forms.ModelForm):
    class Meta:
        model=category
        fields='__all__'