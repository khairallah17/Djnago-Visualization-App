# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib.backends.backend_agg as FigureCanvasAgg
# import os
# from django.shortcuts import HttpResponse
# from . import settings

# def linePlot(request, xText, yText, fileData) :
#     fig = plt.figure(figsize=(10, 6))
#     sns.lineplot(x=xText, y=yText, data=fileData, color='b')
    
#     plt.xlabel(xText)
#     plt.ylabel(yText)
    
#     plt.legend()
    
#     file_path = os.path.join(settings.MEDIA_ROOT, 'line_plot.png')
#     canvas = FigureCanvasAgg(fig)
#     canvas.print_figure(file_path)
    
#     with open(file_path, 'rb') as image_file:
#         response = HttpResponse(image_file.read(), content_type='image/png')

#     return response
from django.shortcuts import render
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from django.http import HttpResponse
import os
from . import settings
from io import BytesIO
import base64

def line_plot():
    
 # Create a simple line plot using Matplotlib
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4, 5], [2, 3, 5, 7, 11])

    # Save the plot as an image in BytesIO
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the image in base64
    image_data = base64.b64encode(buffer.read()).decode('utf-8')

    # Close the Matplotlib figure to free up resources
    plt.close(fig)

    # Create an HTML response with the image
    response = f'<img src="data:image/png;base64,{image_data}">'
    return response
