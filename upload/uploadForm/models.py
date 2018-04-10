from django.db import models
import uuid
from django.db.models import(
    UUIDField,
    CharField,
    TextField,
    IntegerField,
    BooleanField,
    DateTimeField,
    ImageField

)
# Create your models here.
class uploadForm(models.Model):
    AID = CharField(max_length=100)  
    Name = CharField(max_length=100)  
    Genre = CharField(max_length=100)  
    Type = CharField(max_length=100)
    Episodes= CharField(max_length=100)
    Ratings = CharField(max_length=100)  
    Members= CharField(max_length=100)  


