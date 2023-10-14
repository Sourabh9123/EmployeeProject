from django.contrib import admin
from employee_app.models import Employee



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'name', 'age', 'department']
    list_display_links = ['employee_id','name']


admin.site.register(Employee, EmployeeAdmin)