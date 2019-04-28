from django.shortcuts import render
from django.http import HttpResponse
from .models import Data, Client
from geopy.geocoders import Nominatim
import gmaps




def clientshow(request):
    if(request.method == 'GET'):
        
        try:
            clientsdata = Client.objects.all().order_by("-pk")  
            context = {'clientsdata': clientsdata}
            return render(request, 'clientsview.html', context)
        except:   
            return HttpResponse("<br><h3> There is no client data in the data base. Register some clients and try again </h3>") 

        
            
def datashow(request,pk):
    if(request.method == 'GET'):
        energy_value = 0
        client = Client.objects.get(pk = pk)  
        clientdataobject = Data.objects.filter(client = client).order_by("-pk")
        client_data = Data.objects.filter(client=client).order_by("-pk")
        
        if client_data:
            energy_value = Data.objects.filter(
                client = client).order_by("-pk")[0].energy

        context = {'clientdataobject': clientdataobject, 'client': client, 'energy_value': energy_value}
        
        print(clientdataobject[0].longitude)
        print(clientdataobject[0].latitude)
        
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
                
        if(device_serial and vb_meter and va_meter and
            vin_house and cb_meter and ca_meter and cin_house and 
                energy and latitude and longitude):
            
            latfloat = float(latitude)
            longfloat = float(longitude)
            
            print('LATITUDE:', latfloat)
            print('LONGITUDE:', longfloat)

            if((latfloat == 0) and (longfloat == 0)):
                location_address = 'Null'  
            else:
                latlng = latitude + ',' + longitude
                geolocator = Nominatim(user_agent='gpslocator')
                location = geolocator.reverse(latlng)
                location_address = location.address
                 
                
            client_object = Client.objects.get(device_serial = device_serial)    
                
            Data(
                client = client_object, 
                vb_meter = vb_meter,
                va_meter = va_meter, 
                vin_house = vin_house, 
                cb_meter = cb_meter,  
                ca_meter = ca_meter,
                cin_house = cin_house, 
                energy = energy, 
                latitude = latitude, 
                longitude = longitude, 
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
        
        
        
