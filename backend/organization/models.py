from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=350)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    phone_no = models.IntegerField()
    email = models.EmailField()
    website = models.URLField()
    gst_no = models.CharField(max_length=15)
    
    
    def __str__(self):
        return self.name