from django.shortcuts import render
from .form import Student_regisition
# Create your views here.
def showfordata(request):
    fm=Student_regisition()

    return render(request,'index.html',{'form':fm})