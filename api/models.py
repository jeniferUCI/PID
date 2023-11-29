from django.db import models

class Task(models.Model):
    title = models.CharField(max_length= 100, null=True, blank = True, name = 'title')
    body = models.CharField(max_length = 100, null =False, blank = False, name = 'body')
    date = models.DateField(auto_now_add = True, name='date')
