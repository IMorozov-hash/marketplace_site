from django.shortcuts import render

def home(request):
    return render(request, 'main/home_page.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')