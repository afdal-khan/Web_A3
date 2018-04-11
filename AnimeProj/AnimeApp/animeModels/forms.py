from django import forms
from .document import Document

class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = Document
        exclude = ()