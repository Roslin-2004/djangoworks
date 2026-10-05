from django.shortcuts import render

# Create your views here.
from django.views import View
class Homes(View):
    def get(self,request):
        return render(request,'Home.html')
class Add(View):
    def get(self,request):
        return render(request, 'Add.html')
    def post(self, request):
        data=request.POST
        num1=int(data['num1'])
        num2=int( data['num2'])
        result=num1+num2
        context = {'result':result}
        return render(request, 'Add.html',context)
class Fact(View):
    def get(self,request):
        return render(request, 'Factorial.html')
    def post(self, request):
        data=request.POST
        num=int(data['num'])
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        context = {'fact':fact}
        return render(request, 'Factorial.html',context)
class Bmi(View):
    def get(self,request):
        return render(request, 'Bmi.html')
    def post(self, request):
        data=request.POST
        w=int(data['w'])
        h= int(data['h'])
        bmi=w/(h*h)
        context = {'bmi':bmi}
        return render(request, 'Bmi.html',context)
