from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import FloatField, Sum, F
import csv, io
from .models import FileUploadData

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':

        if len(request.POST.getlist('overwrite')) > 0:
            FileUploadData.objects.all().delete()
        
        csv_file = request.FILES['file']
        
        file_data = csv_file.read().decode('UTF-8')
        input_string = io.StringIO(file_data)
        # skip the header
        next(input_string)

        for column in csv.reader(input_string, delimiter='\t'):
            _, data = FileUploadData.objects.update_or_create(
                    item = column[0],
                    item_description = column[1],
                    item_price = column[2],
                    item_count = column[3],
                    vendor = column[4],
                    vendor_address = column[5]
                )
        response = FileUploadData.objects.aggregate(total_revenue = Sum(F('item_price') * F('item_count'), output_field = FloatField()))['total_revenue']

    return render(request, 'upload.html', {'total_revenue': response})