from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import movie


def index(request):
    movie1=movie.objects.all()
    context={'movie_list':movie1}
    return render(request,'index.html',context)
def details(request,movie1_id):
    mov=movie.objects.get(id=movie1_id)
    return render(request,"details.html",{'mov':mov})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description = request.POST.get('description')
        image= request.FILES['image']
        year = request.POST.get('year')
        movies=movie(name=name,description=description,image=image,year=year)
        movies.save( )
    return render(request,'add.html')
def update(request, id):
    movie1=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request, 'edit.html',{'form':form, 'movie1':movie1})
def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')