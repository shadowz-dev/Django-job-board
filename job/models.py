from django.db import models

# Create your models here.

'''
Django Model fields:
    - html widget
    - Validation
    - db size 
    - 

'''
# Choices of job_type 
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model): # talble
    title = models.CharField(max_length=100) # Column creation
#   location= 
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE) # Text Field with choices
    description = models.TextField(max_length=1000) # Text field for big string fields 
    publish_date = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

def __str__(self):  # change "Class object" definition to job title
    self.title