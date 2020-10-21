from django.db import models
from delivery.models import Employee

class Capture(models.Model):
    face = models.TextField()
    employee_number = models.OneToOneField('delivery.Employee', models.DO_NOTHING, db_column='employee_number', primary_key=True)

    class Meta:
        managed = False
        db_table = 'capture'