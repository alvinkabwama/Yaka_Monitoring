from django.db import models
 
    
class Data(models.Model): 
    device_serial = models.CharField(max_length = 255)
    vb_meter = models.CharField(max_length = 255)
    va_meter = models.CharField(max_length = 255)
    vin_house = models.CharField(max_length = 255)
    cb_meter = models.CharField(max_length = 255)
    ca_meter = models.CharField(max_length = 255)
    cin_house = models.CharField(max_length = 255)
    energy = models.CharField(max_length = 255)
    received_at = models.DateTimeField(auto_now_add =True)  
    latitude = models.CharField(max_length = 255)
    longitude = models.CharField(max_length = 255)  
    location = models.CharField(max_length = 255, default = 'Kampala')
    owner = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.device_serial
    
    
     

