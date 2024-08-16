import phonenumbers 
import opencage
import folium 
number = phonenumbers.parse(input('YOU PHONE NUMBER '))
print(number)
from phonenumbers import carrier
carier = carrier.name_for_number(number , 'en')
print(f'Operadora : {carier}')
from phonenumbers import geocoder
loc = geocoder.description_for_number(number , 'en')
print(f' localização : {loc} ')
from opencage.geocoder import OpenCageGeocode
key = '465210746090468285a4b2224963ca3c'
geocoder = OpenCageGeocode(key)
query = str(loc)
result = geocoder.geocode(query)
#print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat , lng)
myMap = folium.Map(loc = [lat , lng] , zoom_start = 9)
folium.Marker([lat , lng] , popup = loc).add_to(myMap)

myMap.save('localizacao.html')
