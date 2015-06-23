from django.db import models 
from django.forms.fields import SplitDateTimeField
from django.forms.models import ModelForm


# test 1
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    def __str__(self):              
        return self.name
   
    
class Project(models.Model):
    name = models.CharField(max_length=30)
    principal =  models.ForeignKey(Person)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    description = models.CharField(max_length=100)
    funding_source = models.CharField(max_length=100)
    funding_allocation = models.CharField(max_length=30)
    research_code = models.CharField(max_length=30)
    member = models.ManyToManyField(Person, related_name='project_member')
    def __str__(self):              
        return self.name   
    def get_start_date(self):
        return self.start_date


    
class Dataset(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    owner = models.ForeignKey(Person, related_name='ds_owner')
    creator = models.ForeignKey(Person, related_name='ds_creator')
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    tools = models.CharField(max_length=30)
    coverage_start_date = models.DateTimeField('coverage start date')
    coverage_end_date = models.DateTimeField('coverage end date')
    coverage_space = models.CharField(max_length=30)
    format = models.CharField(max_length=30)
    keywords = models.CharField(max_length=30)
    citations = models.CharField(max_length=30)
    host_department = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    number_of_files = models.IntegerField(default=0)
    space = models.CharField(max_length=30)
    retention_end_date = models.DateTimeField('retention end date')
    release_date = models.DateTimeField('release date')
    access_permission = models.CharField(max_length=30)
    method_of_sharing = models.CharField(max_length=30)
    def __str__(self):              
        return self.name   

    
class Ethics_Document(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    approval_number = models.CharField(max_length=30)
    consenting_body = models.CharField(max_length=30)
    approval_date = models.DateTimeField('approval date')
    def __str__(self):              
        return self.name   


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'project', 'owner', 'start_date', 'end_date', 'tools']
       
    
    
    