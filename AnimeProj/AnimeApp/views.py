
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .animeModels import Anime
from .forms import UploadForm
import csv
from .animeModels.csv import ParseFile
from django.core.files import File






# Create your views here.
def index(request):
    #listing = Anime.readAll()
    
    args={
        'animes': Anime.objects.all()
    }

    return render(request,'list.html', args)

# def detail(request):
   
#     target = Anime.objects.filter(AID='32281')
#     args ={
#         'anime': target
#     }

#     return render(request, 'details.html', args)

def update(request, anime_id):
    if request.method == "POST":
        print (request.POST.keys())
        print (request.POST.values())
        print (request.POST)
        anime = Anime.objects.get(AID = anime_id)
    
    return render(request, 'update.html' )

def upload(request):
    form = UploadForm()

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            handle_upload(request.FILES['file'])
            return redirect('/')
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {'form': form})

def handle_upload(f):

    with open('/assets/data/anime.csv', 'w') as dest:
        for chunk in f.chunks():
            dest.write(chunk)


    content = []
    content = ParseFile.csvToDict()
    for data in content:
        o = Anime (
            data['ID'],
            data['Name'],
            data['Genre'],
            data['Type'],
            data['Episodes'],
            data['Ratings'],
            data['Members']
        )
        o.save()

# def  readAll():
    #      listings= []
    #      AnimeObj=[]
    #      listings =ParseFile.csvToDict() 
    #      counter = 1
    #      for data in listings:
    #          #print (data)
    #          #put into anime objects
             
    #          current= Anime(data['ID'], data['Name'],data['Genre'],data['Type'],data['Episodes'],data['Ratings'],data['Members'])
    #          current.save()
    #          counter = counter + 1
    #          print(current.Name)
    #      print("DONE")
    #      return listings