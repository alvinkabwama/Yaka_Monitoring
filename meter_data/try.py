import requests



latitude = '0.3324567'
longitude = '32.123467'

latlng = latitude + ',' + longitude


'''

print(latlng)

result = {}
url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={}'
request = url.format(latlng)
data = requests.get(request).json()

result = data['results'][0]


from pygeocoder import Geocoder

location = Geocoder.reverse_geocode(0.332437,32.12345)
print("City:",location.city)
print("Country:",location.country)





from geopy.geocoders import GoogleV3
geocoder = GoogleV3(api_key = 'AIzaSyAH6Tx3JJQvAkt4Tbw3tBWiSO8bLFrN41w')
location_list = geocoder.reverse(0.332437,32.12345)
location = location_list[0]
address = location.address


latitude = '0.3324567'
longitude = '32.123467'

latlng = latitude + ',' + longitude


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="try.py")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)


'''
from ipywidgets.embed import embed_minimal_html
import gmaps
    
latfloat = float('0.33234566')
longfloat = float('32.3456778')

gmaps.configure(api_key='AIzaSyAH6Tx3JJQvAkt4Tbw3tBWiSO8bLFrN41w')
coordinates = (latfloat, longfloat)

mapfig = gmaps.figure(center=coordinates, zoom_level=12)
embed_minimal_html('export.html', views=[mapfig])

mapfig.savefig('Maps.png', dpi=300)

