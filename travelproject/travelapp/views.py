from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import guid
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=guid.objects.all()
    return render(request, 'index.html',{'result':obj,'result1':obj1})
   # return HttpResponse("hello world")
   #name='india'

#def about(request):
#    return render(request,'ab.html')
#   x=int(request.GET['n1'])
 #   y=int(request.GET['n2'])
  #  res=x+y
   # return render(request,'result.html',{'result':res})