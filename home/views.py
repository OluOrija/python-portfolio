from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def index(request):
    return render(request, 'index.html', {})    

def contact(request):
    return render(request, 'contact.html', {})        

def about(request):
    return render(request, 'about.html', {})            

def comingsoon(request):
    return render(request, 'coming-soon.html', {})        