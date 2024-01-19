from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Reviews
# Create your views here.
def demo(request):
    name="USER"
    obj=Place.objects.all()
    rev=Reviews.objects.all()
    return render(request,"index.html",{'result': obj,'reviews':rev})
