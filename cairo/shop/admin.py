from django.contrib import admin
from shop.models import item, department, details
# Register your models here.
admin.site.register(item)
admin.site.register(department)
admin.site.register(details)
