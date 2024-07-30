from django import forms
from .models import MaterialDetail

class MaterialDetailForm(forms.ModelForm):
    class Meta:
        model = MaterialDetail
        fields = ['specification', 'is_heading','quantity', 'make', 'purpose', 'price', 'total', ]
