from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","contact", 'position', 'status'

admin.site.register(Employee,EmployeeAdmin)
