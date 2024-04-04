from django.shortcuts import render
from django.http import JsonResponse
from . import mltool

# Create your views here.
def mySite(request):
    return render(request, 'MyAPI/graph.html')

def myForm():
    return 0

def status():
    return 0

def fetchAPI(request):
    predictions = mltool.generate_jdict()
    return JsonResponse(predictions)