from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'portfolio/home.html')
def projects_view(request):
    return render(request, 'portfolio/projects.html')
def skills_view(request):
    return render(request, 'portfolio/skills.html')
def polls(request):
    return HttpResponse("Polls page")