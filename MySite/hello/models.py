from django.db import models


class Person(models.Model):
    first_name=models.CharField(max_length = 50)
    last_name=models.CharField(max_length = 30)
    height=models.IntegerField()
    weight=models.IntegerField()
    birth_date=models.DateField()
    
    class Meta:
        db_table="person"

    def __str__(self):
        return self.firstname + self.last_name
    
# Create your models here.