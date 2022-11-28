from django.shortcuts import render
from .dropAds import DropAddress



# home page rendering function
def home(request): 
     #collect values fro the html inputs
     if request.method == 'POST':
          number = request.POST['number']
          program = request.POST['program']
          year = request.POST['year']

     #refers to the class it called from (DropAddress)
          address =DropAddress(numInClass=number,program=program,year=year)
          address.genAddress()

     return render (request, 'templates\index.html')