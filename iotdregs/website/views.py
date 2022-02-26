from logging.handlers import RotatingFileHandler
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = request.POST
        return render(request, "website/index.html", {
            "data": data,
        })

    return render(request, "website/index.html")
