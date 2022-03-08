from django.db import models

# Create your models here.
class Task(models.Model):
    #student_info
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(blank=True, null=True) #description
    e_mail = models.TextField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)
    count = models.TextField(blank=True, null=True)
    check_in_time = models.DateTimeField(auto_now_add=True) #check_in_time

    def __str__(self):
        #return the task title
        return self.first_name