from django.db import models
import uuid




class Employee(models.Model):
    employee_id = models.AutoField( editable=False, primary_key=True)
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=150)
    

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    

    def __str__(self):
        return self.name
    
