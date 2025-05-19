from django.shortcuts import render

def home(request):
    return render(request, 'tree_menu/home.html')

def about(request):
    return render(request, 'tree_menu/about.html')
