import csv
import os

class ParseFile:

    def csvToDict():
        #read csv file
        CSVFile= csv.DictReader(open("/home/adminuser/Downloads/AnimeProj/AnimeProj/AnimeApp/static/anime.csv","r"))
        listings= [] #empty array to store all 12000 records as one
        current ={}

        #print(CSVFile)

        for line in CSVFile:
            current={}
            current['ID'] =line['anime_id']
            current['Name']= line['name']
            current['Genre'] =line['genre']
            current['Type']= line['type']
            current['Episodes'] = line['episodes']
            current['Ratings'] =line['rating']
            current['Members'] =line['members']
            
            #put lines into listing dictionary
            listings.append(current)
        return listings
