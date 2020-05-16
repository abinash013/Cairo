from django.db import models
import datetime

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=20)
    department_description=models.CharField(max_length=400)
    def __str__(self):
        return self.department_name

class item(models.Model):
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image=models.CharField(max_length=40)
    description = models.CharField(max_length=600)
    def __str__(self):
        return self.item_name
