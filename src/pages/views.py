from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def home_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  my_context = {
      "my_text"     : "This is about us",
      "description" : "This is a description",
      "list_items"  : [1, 2, 3, 4]  
  }
  #return HttpResponse("<h1>Contact!</h2>")
  return render(
      request,
      "home.html", # Name template
      my_context
  )

def contact_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  return HttpResponse("<h1>Contact!</h2>")
