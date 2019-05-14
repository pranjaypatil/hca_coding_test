from django.shortcuts import render
from django.db.models import FloatField, Sum, F
from django.utils.datastructures import MultiValueDictKeyError
import csv, io
from .models import FileUploadData

# Create your views here.
def index(request):
    return render(request, 'index.html')

def upload(request):
    error_reason = ''
    response = 0

    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        try:
            if len(request.POST.getlist('overwrite')) > 0:
                FileUploadData.objects.all().delete()

            csv_file = request.FILES['file']

            file_data = csv_file.read().decode('UTF-8')
            input_string = io.StringIO(file_data)
            # skip the header
            next(input_string)

            for column in csv.reader(input_string, delimiter='\t'):
                _ = FileUploadData.objects.create(
                        item = column[0],
                        item_description = column[1],
                        item_price = column[2],
                        item_count = column[3],
                        vendor = column[4],
                        vendor_address = column[5]
                    )
        except IndexError:
            error_reason = 'File format not correct, please check for valid TSV format'
        except MultiValueDictKeyError:
            error_reason = 'No file was uploaded, please select a file in file chooser and try again. Click the button below to navigate to file upload page.'
        response = FileUploadData.objects.aggregate(total_revenue = Sum(F('item_price') * F('item_count'), output_field = FloatField()))['total_revenue']
        response = response if response is not None else 0
    return render(request, 'upload.html', {'total_revenue': response, 'error': error_reason})
