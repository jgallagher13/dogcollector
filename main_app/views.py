from django.shortcuts import render

dogs = [
  {'name': 'Socks', 'breed': 'German Shepherd/ Greyhound', 'description': 'long and lanky', 'age': 3},
  {'name': 'Obi-wan', 'breed': 'Cattle Dog', 'description': 'wild and snuggly', 'age': 2},
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })