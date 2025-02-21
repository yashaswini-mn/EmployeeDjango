from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Employees
from django.contrib import messages

# Create your views here.
def employee_list(request):
    if request.method=='POST':
        empname = request.POST.get('empname')
        empmail=request.POST.get('empmail')
        pno = request.POST.get("pno")
        department=request.POST("department")
        designation=request.POST("designation")
        salary=request.POST("salary")
        date=request.POST("date")
        empType=request.POST("empType")
        address=request.POST("address")
        status=request.POST("status")

        employee=Employees(empname=empname,empmail=empmail,pno=pno,department=department,designation=designation,salary=salary,date=date,empType=empType,address=address, status=status )

        employee.save()
        return redirect('employee_list')
    employees= Employees.objects.all()
    return render(request, 'index.html', {'employees':employees})

def update_employee(request, pk):
    employee = get_object_or_404(Employees, pk=pk)
    if request.method=='POST':
        empname = request.POST.get('empname')
        empmail=request.POST.get('empmail')
        pno = request.POST.get("pno")
        department=request.POST("department")
        designation=request.POST("designation")
        salary=request.POST("salary")
        date=request.POST("date")
        empType=request.POST("empType")
        address=request.POST("address")
        status=request.POST("status")

        employee.empname =empname
        employee.empmail=empmail
        employee.pno =pno
        employee.department=department
        employee.designation=designation
        employee.salary=salary
        employee.date=date
        employee.empType=empType
        employee.address=address
        employee.status=status
    
        employee.save()
        messages.success(request,"Updated")
        return redirect('employee_list')
    return render(request, 'update_employee.html',{'employee':employee} )

def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    messages.success(request,"Deleted")
    return redirect('student_list')