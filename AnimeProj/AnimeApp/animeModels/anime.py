import csv
import uuid
from django.db import models
from django.db.models import (
UUIDField,
CharField, 
IntegerField,
BooleanField,
DateTimeField,
DecimalField
)
from .csv import ParseFile


class Anime(models.Model):
    AID = CharField(max_length=100)  
    Name = CharField(max_length=100)  
    Genre = CharField(max_length=100)  
    Type = CharField(max_length=100)
    Episodes= CharField(max_length=100)
    Ratings = CharField(max_length=100)  
    Members= CharField(max_length=100)  


    @staticmethod 
    def  readAll():
         listings= []
         AnimeObj=[]
         listings =ParseFile.csvToDict() 
         counter = 1
         for data in listings:
             #print (data)
             #put into anime objects
             
             current= Anime(data['ID'], data['Name'],data['Genre'],data['Type'],data['Episodes'],data['Ratings'],data['Members'])
             current.save()
             counter = counter + 1
             print(current.Name)
         print("DONE")
         return listings

    # def __str__(self):
    #     return Anime.Name
