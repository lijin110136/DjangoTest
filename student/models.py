from django.db import models
from django.contrib import admin

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=100)
    sage = models.IntegerField(max_length=10)

    def __unicode__(self):
        return self.sname

    class Meta:
        ordering = ["sname"]
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'sname', 'sage')
    list_filter = ('sname',)
    search_fields = ('sname',)
    ordering = ('-id',)
admin.site.register(Student, StudentAdmin)
    

