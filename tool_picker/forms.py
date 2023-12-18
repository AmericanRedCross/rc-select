from django import forms
from .models import ToolPicker

class ToolSelectionForm(forms.ModelForm):
    class Meta:
        model = ToolPicker
        fields = ['intended_use_type', 'available_budget']
