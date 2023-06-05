from harversine import harversine
from LocationFactory import LocationFactory


   

def calculate_distance(city1, country1, city2, country2, option):
  factory = LocationFactory()
  service = factory.getService(option)

  lat1, lon1 = service.get_lat_long(city1, country1)
  lat2, lon2 = service.get_lat_long(city2, country2)
  return harversine(float(lat1), float(lon1), float(lat2), float(lon2))
  
city_1 = input("Ingrese la ciudad 1: ")
country_1 = input("Ingrese el pais 1: ")
city_2 = input("Ingrese la ciudad 2: ")
country_2 = input("Ingrese el country 2: ")

print("Seleccione el tipo de servicio: ")
print("[1] CSV")
print("[2] API")
print("[3] Mock")
service_type = int(input("Ingrese el número de la opcion: "))
distance = calculate_distance(city_1,country_1,city_2,country_2,service_type)
print("Distancia entre ciudades: ", distance)