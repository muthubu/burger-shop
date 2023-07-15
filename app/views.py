from django.shortcuts import render


def home(request):
   return render(request,'home.html')

def trys(request):
   return render(request,'try.html')


