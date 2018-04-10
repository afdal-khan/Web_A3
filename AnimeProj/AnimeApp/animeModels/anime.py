import csv
import uuid
from .csv import ParseFile
from django.db import models
from django.db.models import (
UUIDField,
CharField, 
IntegerField,
BooleanField,
DateTimeField,
DecimalField
)



class Anime(models.Model):
    AID = CharField(max_length=100)  
    Name = CharField(max_length=100)  
    Genre = CharField(max_length=100)  
    Type = CharField(max_length=100)
    Episodes= CharField(max_length=100)
    Ratings = CharField(max_length=100)  
    Members= CharField(max_length=100)  
    
    def __str__(self):
        return self.Name