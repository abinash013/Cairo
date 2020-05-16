from django.shortcuts import render
from .models import department,item

# Create your views here.
def home(request):
    return render(request, 'shop/homepage.html', context=None)

def index(request,dname):
    try:
        dept=department.objects.get(department_name=dname)
    except department.DoesNotExist:
        dept=None
    return render(request,"shop/index.html",{'dept':dept})
