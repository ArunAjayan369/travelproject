from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import next

# Create your views here.

def demo(request):
    obj= place.objects.all()
    obj2= next.objects.all()


    return render(request,"index.html",{'result':obj,'result2':obj2})
# def addition(request):
#     x=int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res= x+y
#     return render(request,"result.html",{'result':res})
# # def about(request):
# #     return render(request,"result.html")
# # def contact(request):
# #     return HttpResponse("hello am contact")


