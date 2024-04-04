from django.shortcuts import render
from django.http import JsonResponse
from . import mltool

# Create your views here.
def mySite(request):
    return render(request, 'MyAPI/graph.html')

def About():
    return render(request, "MyAPI/about.html")


def fetchAPI(request):
    predictions = mltool.generate_jdict()
    return JsonResponse(predictions)