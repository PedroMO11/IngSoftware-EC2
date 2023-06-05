import requests
import csv

class ILatLong:
    def get_lat_long(self,city, country):
      pass

class CSV(ILatLong):
  def get_lat_long(self,city, country):
    with open('worldcities.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city'] == city and row['country'] == country:
                return row['lat'], row['lng']
    
class API(ILatLong):
  def get_lat_long(self,city, country):
    response = requests.get("https://nominatim.openstreetmap.org/search?q="+city+","+country+"&format=json")
    return response.json()[0]['lat'], response.json()[0]['lon']

class Mock(ILatLong):
  def get_lat_long(self,city, country):
       return "55.7504461", "37.6174943"
   
