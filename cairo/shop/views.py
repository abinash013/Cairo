from django.shortcuts import render
from .models import department, details
from .forms import signinform
# Create your views here.
def home(request):
    return render(request, 'shop/homepage.html', context=None)

def index(request,dname):
    try:
        dept = department.objects.get(department_name=dname)
    except department.DoesNotExist:
        dept = None
    return render(request,"shop/index.html",{'dept':dept})

def signin(request):
    return render(request, 'shop/signin.html', context=None)

def siginprocess(request):
    if (request.method=="POST"):
        currentform=signinform(request.POST)
        if currentform.is_valid():
            currentform.save()
            return render(request,'shop/homepage.html',context=None)
    else:
        form=signinform()
    return render(request,'shop/signin.html',context=None)
