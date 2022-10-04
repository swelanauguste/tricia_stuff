from django import forms

from .models import Contract


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"
        widgets = {
            'start_date': forms.TextInput(attrs={"type": "date"}),
            'end_date': forms.TextInput(attrs={"type": "date"}),
        }
