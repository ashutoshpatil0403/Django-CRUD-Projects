from django.shortcuts import render,redirect
from .models import UPSC_Books
from .form import AddUPSCBooks
from django.views import View

# # Create your views here.

# class home(View):
#     def get(self,request):
#         return render(request,'base.html')

def home(request):
    UPSC=UPSC_Books.objects.all()
    return render(request,'home.html',{'UPSCdata':UPSC})

def addbook(request):
    fm=AddUPSCBooks()
    # fm=UPSC_Books.objects.all()
    fm=AddUPSCBooks(request.POST)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    else:
        return render(request,'addbook.html',{'upscform':fm})
    print(fm)
    return render(request,'addbook.html',{'upscform':fm})

def deletebook(request,id):
    U=UPSC_Books.objects.get(pk=id)
    U.delete()  
    return redirect('/')

def updatebook(request,id):
    oldbook=UPSC_Books.objects.get(pk=id)
    fm=AddUPSCBooks(instance=oldbook)
    
    if request.method=='POST':
        fm=AddUPSCBooks(request.POST,instance=oldbook)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    
    return render(request,'update.html',{'upscform':fm})




