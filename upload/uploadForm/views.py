from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import uploadForm
from .forms import Upload

# Create your views here.
def index(request):
    allRecords = uploadForm.objects.all()
    return render(request, 'list.html', {
        'uploadForm': allRecords
    })


from django.http import HttpResponseRedirect

class RecordView(View):

    def get(self, request):
        UForm = Upload()
        return render(request, 'add.html', {
            'form' : UForm
        })

    def post(self, request):
        UForm = Upload(request.POST, request.FILES)
        if UForm.is_valid():
            UForm.save()
            return HttpResponseRedirect("/?oper=cat&res=true")
        # Else request was invalid
        return render(request, 'add.html', {
            'form' : UForm
        })
