from django.db import models

# Create your models here.
class Dept(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)

    


class Emp(models.Model):
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    EmpNo=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField()

    

