from django.urls import path
from employee_app.views import (HomePageView,EmployeesView,AddEmployeeView,
                                 RemoveAnEmployee, FilterEmployee
                                )


urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('employees',EmployeesView.as_view(), name='get_all_employees' ),
    path('addemployee',AddEmployeeView.as_view(), name='add_employees' ),
    path('removeemployee',RemoveAnEmployee.as_view(), name='remove_employees' ),
    path('searchemployee',FilterEmployee.as_view(), name='search_employees' ),
    



]
