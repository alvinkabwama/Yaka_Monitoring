from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from geopy.geocoders import Nominatim
import gmaps

def datashow(request):
    if(request.method == 'GET'):
        serialnumber = '0645'
        devicedata = Data.objects.filter(client.device_serial = serialnumber).order_by("-pk")
        
        
        context = {'devicedata': devicedata}
        return render(request, 'tableview.html', context)
        
    
def datareceive(request):
    if(request.method == 'GET'):
        device_serial = request.GET.get("device_serial")
        vb_meter = request.GET.get("vb_meter")
        va_meter = request.GET.get("va_meter")
        vin_house = request.GET.get("vin_house")
        cb_meter = request.GET.get("cb_meter")
        ca_meter = request.GET.get("ca_meter")
        cin_house = request.GET.get("cin_house")
        energy = request.GET.get("energy")
        latitude = request.GET.get("latitude")
        longitude = request.GET.get("longitude")   
        owner = request.GET.get("owner")
        
        print(device_serial)
        print(vb_meter)
        print(va_meter)
        print(vin_house)
        print(cb_meter)
        print(ca_meter)
        print(cin_house)
        print(energy)
        print(latitude)
        print(longitude)   
        print(owner)
                
        if(device_serial and vb_meter and va_meter and
            vin_house and cb_meter and ca_meter and cin_house and 
                energy and latitude and longitude and owner):
            latfloat = float(latitude)
            longfloat = float(longitude)

            if((latfloat == 0) and (longfloat == 0)):
                location_address = 'Null'  
            else:
                latlng = latitude + ',' + longitude
                geolocator = Nominatim(user_agent='gpslocator')
                location = geolocator.reverse(latlng)
                location_address = location.address
                 
            Data(
                device_serial = device_serial, 
                vb_meter = vb_meter,
                va_meter = va_meter, 
                vin_house = vin_house, 
                cb_meter = cb_meter,  
                ca_meter = ca_meter,
                cin_house = cin_house, 
                energy = energy, 
                latitude = latitude, 
                longitude = longitude, 
                owner = owner, 
                location = location_address
            ).save()
                  
            return HttpResponse("<br><h3> Pass </h3>")
        else:
            return HttpResponse("<br><h3> Data Missing </h3>")
        
def maps_view(request,pk):
    device_data = Data.objects.get(pk = pk)
    latfloat = float(device_data.latitude)
    longfloat = float(device_data.longitude)
    
    gmaps.configure(api_key='AIzaSyAH6Tx3JJQvAkt4Tbw3tBWiSO8bLFrN41w')
    new_york_coordinates = (latfloat, longfloat)
    gmaps.figure(center=new_york_coordinates, zoom_level=12)

    return render(request, 'mapsview.html')
        
def datasend(request):
    if(request.method == 'GET'):
        return render(request, 'datasend.html')
        
        
        
