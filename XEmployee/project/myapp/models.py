from django.db import models

# Create your models here.
class Employees(models.Model):
    id=models.AutoField(primary_key=True)
    empname=models.TextField()
    empemail=models.EmailField()
    pno=models.IntegerField()
    department=models.TextField(max_length=200)
    designation=models.TextField(max_length=200)
    salary=models.IntegerField()
    date=models.DateField()
    empType=models.TextField()
    address=models.TextField()
    status=models.BooleanField()

    def __str__(self):
        return self.name
    
