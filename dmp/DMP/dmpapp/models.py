from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models 
from django.forms.models import ModelForm, ModelMultipleChoiceField


# test 1
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40,null=True)
    phone = models.CharField(max_length=40,null=True)
    def __str__(self):              
        return self.name
   
    
class Project(models.Model):
    name = models.CharField(max_length=30)
    principal =  models.ForeignKey(Person)
    start_date = models.DateField('start date',null=True)
    end_date = models.DateField('end date',null=True)
    description = models.CharField(max_length=100,null=True)
    funding_source = models.CharField(max_length=100,null=True)
    funding_allocation = models.CharField(max_length=30,null=True)
    research_code = models.CharField(max_length=30,null=True)
    member = models.ManyToManyField(Person, related_name='project_member')
    # hack to get id into the posted form, so I can redirect correctly
    def __str__(self):              
        return self.name   
    def get_start_date(self):
        return self.start_date


    
class Dataset(models.Model):
    name = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=30,null=True)
    project = models.ForeignKey(Project)
    owner = models.ForeignKey(Person, related_name='ds_owner',null=True)
    creator = models.ForeignKey(Person, related_name='ds_creator',null=True)
    start_date = models.DateField('start date',null=True)
    end_date = models.DateField('end date',null=True)
    tools = models.CharField(max_length=30,null=True)
    coverage_start_date = models.DateField('coverage start date',null=True)
    coverage_end_date = models.DateField('coverage end date',null=True)
    coverage_space = models.CharField(max_length=30,null=True)
    format = models.CharField(max_length=30,null=True)
    keywords = models.CharField(max_length=30,null=True)
    citations = models.CharField(max_length=30,null=True)
    host_department = models.CharField(max_length=30,null=True)
    location = models.CharField(max_length=30,null=True)
    number_of_files = models.IntegerField(default=0,null=True)
    space = models.CharField(max_length=30,null=True)
    retention_end_date = models.DateField('retention end date',null=True)
    release_date = models.DateField('release date',null=True)
    access_permission = models.CharField(max_length=30,null=True)
    method_of_sharing = models.CharField(max_length=30,null=True)
    def __str__(self):              
        return self.name   

    
class Ethics_Document(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    approval_number = models.CharField(max_length=30)
    consenting_body = models.CharField(max_length=30)
    approval_date = models.DateField('approval date')
    def __str__(self):              
        return self.name   


class DatasetForm(ModelForm):
    class Meta:
        model = Dataset
        fields = ['name', 'project', 'owner','description', 'start_date', 'end_date',
                  'tools','coverage_start_date','coverage_end_date','coverage_space',
                  'format','keywords','citations','host_department','location', 
                  'number_of_files','space','retention_end_date','release_date',  
                  'access_permission','method_of_sharing']  

       
class ProjectForm(ModelForm):
    class Meta:
        model = Project        
        #toppings = forms.ModelMultipleChoiceField(queryset=Person.objects.all())
        fields = ['id','name','principal', 'start_date', 'end_date', 'description',
                  'funding_source','funding_allocation','research_code','member']  
      
    

    