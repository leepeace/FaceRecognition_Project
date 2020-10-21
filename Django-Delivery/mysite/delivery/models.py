from django.db import models
from django.db import connections

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=15)
    company_number = models.CharField(primary_key=True, max_length=15)
    company_phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'company'
    def __str__(self):
        return self.company_number

class Employee(models.Model):
    employee_number = models.CharField(primary_key=True, max_length=15)
    employee_name = models.CharField(max_length=30)
    employee_phone = models.CharField(max_length=30)
    employee_sex = models.CharField(max_length=1)
    company_number = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_number')

    class Meta:
        managed = False
        db_table = 'employee'
        
class Nowcapture(models.Model):
    nowtime = models.DateTimeField(primary_key=True)
    nowcapture = models.TextField()
    todaydate = models.DateField()
    nowpeople = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'nowcapture'
