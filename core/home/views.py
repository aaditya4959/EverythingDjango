from django.shortcuts import render
from django.http import HttpResponse

# this files is used for writing the logic
# Create your views here.

def home(request):
    people = [
        {"name": "John", "age": 20},
        {"name": "Jane", "age": 21},
        {"name": "Jim", "age": 22},
        {"name": "Jill", "age": 23}
    ]
    return render(request, "index.html", context = {"people": people})


def success_page(request):
    return HttpResponse("Success page")