from django import forms
from .models import ToolPicker

class ToolSelectionForm(forms.ModelForm):
    class Meta:
        model = ToolPicker
        fields = ['intended_use_type', 'available_budget', 'setup_time', 'setup_complexity', 'maintenance', 'closeout', 'support', 'performance', 'connectivity', 'data_cleaning', 'data_viz', 'interoperability', 'localization', 'data_privacy', 'data_protection']

class UploadFileForm(forms.Form):
    file = forms.FileField()