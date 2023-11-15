from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import visualization
import os
from . import settings

def index(request):
    return render(request, 'index.html')

def successFile(request):
    return HttpResponse("success")

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        file_directory = os.path.join(settings.BASE_DIR, 'visualizationapp/files')
        
        # Ensure 'files' directory exists; create if not
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)

        file_path = os.path.join(file_directory, uploaded_file.name)

        try:
            # Create the file and write the uploaded content to it
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return HttpResponse('File uploaded successfully!')
        except Exception as e:
            return HttpResponse(f'Error uploading file: {str(e)}')

    return render(request, 'upload.html')



def visualize(request):
    
    image = visualization.line_plot()
    
    return HttpResponse(image, content_type='text/html')