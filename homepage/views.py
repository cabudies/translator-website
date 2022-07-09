from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  # return HttpResponse("Welcome to translation hub...")
  return render(request, 'translator_website/homepage.html')

def about_us(request):
  # return HttpResponse("About us page..")
  return render(request, 'translator_website/about_us.html')


