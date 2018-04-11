
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .animeModels import Anime
from .forms import UploadFileForm
from .models import Document
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
    print (request.POST.keys())
    print (request.POST.values())
    print (request.POST)
    anime = Anime.objects.get(AID = anime_id)
    return render(request, 'update.html',{"el":anime} )
        
    


# def upload(request):
#     form = UploadFileForm()

#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # uploaded_file = request.FILES['file']
        
#             handle_upload(request.FILES['file'])
#             form.save()
#             return redirect('/account/login')
#     else:
#         form = UploadFileForm()
    
#     return render(request, 'upload.html', {'form': form})

def upload(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            handle_upload()
            return redirect('/listings')
    else:
        form = UploadFileForm()

    return render(request,'upload.html',{'form': form})


def handle_upload():

    with open('assets/data/anime.csv', 'r') as data:
        file_data = csv.DictReader(data)
        # for i in dest.readlines():
        #     print (i)
        # for chunk in f.chunks():
        #     dest.write(chunk)
        for row in file_data:
            o = Anime (
            AID = row['anime_id'],
            Name = row['name'],
            Genre = row['genre'],
            Type = row['type'],
            Episodes = row['episodes'],
            Ratings = row['rating'],
            Members = row['members']
        )
        o.save()

        


    # content = []
    # content = ParseFile.csvToDict()
    # for data in content:
    #     o = Anime (
    #         data['anime_id'],
    #         data['name'],
    #         data['genre'],
    #         data['type'],
    #         data['episodes'],
    #         data['ratings'],
    #         data['members']
    #     )
    #     o.save()

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