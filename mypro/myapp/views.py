from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def first(request):
#     return HttpResponse("1st page")
#
#
# def second(request):
#     return HttpResponse("2nd page")
from django.views import View
class First(View):
    def get(self,request):
        return HttpResponse("<h1>first</h1>")
class Second(View):
    def get(self,request):
        return HttpResponse("2st page")
from myapp.models import Person
class First(View):
     def get(self,request):
         data=[{"name":"arun","age":23,"place":"ekm"},
               {"name":"df","age":23,"place":"ekm"},
               {"name":"aiii","age":23,"place":"ekm"}]
         context={'data':data}
         data=Person.object.all()
         return render(request,'first.html',context)
#
#
# class Second(View):
#     def get(self, request):
#         return render(request, 'second.html', context={})

from myapp.models import Movie

class Movie_list(View):
    def get(self,request):
        m=Movie.objects.all()
        print(m)
        context={'movies':m}
        return render(request,'movielist.html',context)
class Add_movie(View):
    def get(self,request):

        return render(request, 'addmovie.html')
    def post(self, request):
        print(request.POST)

        data=request.POST
        n=data['name']
        d = data['director']
        y = data['year']
        print(n,d,y)
        return render(request, 'addmovie.html')
