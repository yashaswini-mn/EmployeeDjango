from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employees
from django.contrib import messages

# Create your views here.
def employee_list(request):
    if request.method=='POST':
        empname = request.POST.get('empname')
        empemail=request.POST.get('empeemail')
        pno = request.POST.get("pno")
        department=request.POST.get("department")
        designation=request.POST.get("designation")
        
        salary=request.POST.get("salary")
        date=request.POST.get("date")
        empType=request.POST.get("empType")
        address=request.POST.get("address")
        status=request.POST.get("status")

        employee=Employees(empname=empname,empemail=empemail,pno=pno,department=department,designation=designation,salary=salary,date=date,empType=empType,address=address, status=status )

        employee.save()
        messages.success(request, "Employee added successfully")
        return redirect('employee_list')
    employees= Employees.objects.all()
    return render(request, 'index.html', {'employees':employees})

def update_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method=='POST':
        empname = request.POST.get('empname')
        empemail=request.POST.get('empemail')
        pno = request.POST.get("pno")
        department=request.POST.get("department")
        designation=request.POST.get("designation")
        salary=request.POST.get("salary")
        date=request.POST.get("date")
        empType=request.POST.get("empType")
        address=request.POST.get("address")
        status=request.POST.get("status")

        employee.empname =empname
        employee.empemail=empemail
        employee.pno =pno
        employee.department=department
        employee.designation=designation
        employee.salary=salary
        employee.date=date
        employee.empType=empType
        employee.address=address
        employee.status=status
    
        employee.save()
        messages.success(request,"Employee Updated Successfully")
        return redirect('employee_list')
    return render(request, 'update_employee.html',{'employee':employee} )

def delete_student(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    employee.delete()
    messages.success(request,"Employee Deleted Successfully")
    return redirect('employee_list')