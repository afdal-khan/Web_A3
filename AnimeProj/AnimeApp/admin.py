from django.contrib import admin

# Register your models here.
from .animeModels import Anime
#from accounts.models import UserProfile
#shows Anime class on django admin page
admin.site.register(Anime)
#admin.site.register(UserProfile)