from django.shortcuts import render


def home(request):
   return render(request,'home.html')

def items(request):
   return render(request,"itemslist.html")   

def trys(request):
   return render(request,'try.html')


