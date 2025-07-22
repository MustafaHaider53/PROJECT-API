from django.contrib import admin
from api.models import Student
# Register youfrom api.models import Studentr models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
      list_display = ['id' , 'name' , 'roll' , 'city']  
