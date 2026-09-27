from django.shortcuts import render
from django.http import HttpResponse

# this files is used for writing the logic
# Create your views here.

def home(request):
    return render(request, "index.html")


def success_page(request):
    return HttpResponse("Success page")