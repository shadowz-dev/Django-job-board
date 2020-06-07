from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):
    job_list = Job.objects.all() # return all jobs inside jobs model db
    context = {'jobs' :job_list } # Template Name in string
    return render(request,'job/job_list.html', context) # render the request in the html with the context





def job_details(request , id):
    job_details = Job.objects.get(id=id)
    context = {'job' :job_details}
    return render(request,'job/job_details.html',context)