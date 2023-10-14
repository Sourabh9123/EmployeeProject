from django.shortcuts import render, redirect
from django.views import View
from employee_app.models import Employee

from django.http import HttpResponse
from django.contrib import messages





class HomePageView(View):

    def get(self, request):
        
        print('done')
        return render(request, 'home.html')




class EmployeesView(View):
    def get(self,request, *args, **kwargs):
        employees = Employee.objects.all() 
        
    
        context = {
            'employees': employees
        }

    
        return render(request, 'employees.html', context=context)



class AddEmployeeView(View):

    def get(elf,request, *args, **kwargs):
        return render(request, 'addemployee.html')

    def post(self,request, *args, **kwargs ):
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')

        if age.isdigit():
            if name and age and department is not None:

                employee = Employee.objects.create(name=name, age=age, department=department)
                employee.save()
                messages.success(request, "Employee saved Successfuly.")
                return redirect('add_employees')
        else:
            messages.error(request, "Please Provide Correct details")
            return redirect('add_employees')
        

        messages.error(request, "Something went worng")
        return redirect('add_employees')
        


        



class RemoveAnEmployee(View):

    def get(self,  request, *args, **kwargs):
        employees = Employee.objects.all()
        context= {
            'employees': employees
        }
        return render(request, 'removeemployee.html', context=context)
    

    def post(self,  request, *args, **kwargs):
        name = request.POST.get('name')
        print(name)
        if name:
            try:
                employee = Employee.objects.filter(name=name).first()
          
                if employee is not None:
                    employee.delete()
                   
                    messages.success(request, "Employee removed successfully.")
                    return redirect('remove_employees')

                else:
                    return HttpResponse( 
                        ' Employee Not Found'
                    )

            except Employee.DoesNotExist:
      
                return HttpResponse('Employee Not Found')
            
        return HttpResponse('No name Provided')





class FilterEmployee(View):
    def get(self, request, *args, **kwargs):
        return render(request ,  'filteremployee.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        
        if name:
            try:
                employee = Employee.objects.filter(name__icontains=name) 
              
                if not employee:

                    messages.success(request, "Employee Does not exists.")
                    return redirect('search_employees')
            

                return render(request ,  'filteremployee.html', {'employees':employee})
            except Employee.DoesNotExist:
                messages.success(request, "Employee Does not exists.")
                return redirect('search_employees')
            
        messages.success(request, "No Name Provided")
        return redirect('search_employees')
            
       