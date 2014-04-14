from django.db import models
from django.contrib import admin

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    sage = models.IntegerField(max_length=10)

    def __str__(self):
        return self.sname

    class Meta:
        ordering = ["sname"]
admin.site.register(Student)
    

