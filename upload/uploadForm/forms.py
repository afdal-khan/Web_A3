from django import forms
from .models import uploadForm

class Upload(forms.ModelForm):
    class Meta:
        model = uploadForm
        exclude = ()
    
    # def save (self, commit=True):
    #     o = Object()
    #     o.attr = self.cleaned_data['attribute-name']

    #     if commit:
    #         o.save()
        
    # return o