from django.db import models

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=20)
    def __str__(self):
        return self.department_name

class item(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=2600)
    def __str__(self):
        return self.item_name

class details(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return self.name
