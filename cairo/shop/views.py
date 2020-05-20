from django.shortcuts import render, reverse
from .models import department, details
from .forms import signinform,loginform
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
        currentform = signinform(request.POST)
        if currentform.is_valid():
            uobj = currentform.cleaned_data
            uemail = uobj["email"]
            if(details.objects.filter(email=uemail).exists()):
                error_message = True
                return render(request, 'shop/signin.html', {'error_message': error_message})
            currentform.save()
            return render(request, 'shop/homepage.html', context=None)
    else:
        currentform = signinform()
    return render(request, 'shop/signin.html', {'currentform': currentform})


def login(request):
    if(request.method=="POST"):
        formInstance = loginform(request.POST)
        if formInstance.is_valid():
            userobj = formInstance.cleaned_data
            uemail = userobj["email"]
            upassword = userobj["password"]
            d = details.objects.get(email=uemail)
            if ((details.objects.filter(email=uemail).exists()) and (d.password == upassword)):
                return render(request, 'shop/signin.html')
            else:
                error_message=True
                return render(request, 'shop/homepage.html', {'error_message':error_message})
