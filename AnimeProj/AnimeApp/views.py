
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .animeModels import Anime




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

        

