from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def home_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  #return HttpResponse("<h1>Contact!</h2>")
  return render(
      request,
      "home.html", # Name template
      {}
  )


def contact_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  return HttpResponse("<h1>Contact!</h2>")
