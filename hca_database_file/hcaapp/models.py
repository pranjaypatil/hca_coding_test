from django.db import models

# Create your models here.
class FileUploadData(models.Model):
    item = models.CharField(max_length=100, null=True)
    item_description = models.CharField(max_length=500, null=True)
    item_price = models.FloatField(null=True)
    item_count = models.IntegerField(null=True)
    vendor = models.CharField(max_length=50, null=True)
    vendor_address = models.CharField(max_length=500, null=True)
