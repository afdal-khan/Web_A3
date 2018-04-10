from django.forms import ModelForm
from.models import uploadForm

class Upload(ModelForm):
    class Meta:
        model = uploadForm
        exclude = ()