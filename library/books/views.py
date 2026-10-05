from django.http.response import JsonResponse
from django.template.context_processors import request
# Create your views here.
from django.shortcuts import render
from django.views import View
from books.models import Book

class Home(View):
    def get(self,request):
        return render(request,'home.html')
class ViewBooks(View):
    def get(self,request):
        books=Book.objects.all()
        context = {'books':books}
        return render(request,'viewbook.html',context)
class Addbook(View):
    def get(self,request):
        return render(request, 'addbook.html')
    def post(self, request):
        data=request.POST
        t=data['title']
        a=data['author']
        l= data['language']
        p=data['pages']
        b=Book.objects.create(title=t,author=a,language=l,pages=p)
        return render(request, 'addmovie.html')


