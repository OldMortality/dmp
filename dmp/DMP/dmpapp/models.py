from django import forms
from django.db import models 
from django.forms.models import ModelForm

# test 1
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40,null=True,blank=True)
    phone = models.CharField(max_length=40,null=True,blank=True)
    def __str__(self):              
        return self.email  ## + ":" + str(self.id)
   
    
class Project(models.Model):
    name = models.CharField(max_length=30)
    principal =  models.ForeignKey(Person)
    start_date = models.DateField('start date',null=True,blank=True)
    end_date = models.DateField('end date',null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    funding_source = models.CharField(max_length=100,null=True,blank=True)
    funding_allocation = models.CharField(max_length=30,null=True,blank=True)
    research_code = models.CharField(max_length=30,null=True,blank=True)
    member = models.ManyToManyField(Person, related_name='project_member')
    # hack to get id into the posted form, so I can redirect correctly
    def __str__(self):              
        return self.name   
    def get_start_date(self):
        return self.start_date


    
class Dataset(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    description = models.CharField(max_length=30,null=True,blank=True)
    project = models.ForeignKey(Project)
    owner = models.ForeignKey(Person, related_name='ds_owner',null=True,blank=True)
    creator = models.ForeignKey(Person, related_name='ds_creator',null=True,blank=True)
    start_date = models.DateField('start date',null=True,blank=True)
    end_date = models.DateField('end date',null=True,blank=True)
    tools = models.CharField(max_length=30,null=True,blank=True)
    coverage_start_date = models.DateField('coverage start date',null=True,blank=True)
    coverage_end_date = models.DateField('coverage end date',null=True,blank=True)
    coverage_space = models.CharField(max_length=30,null=True,blank=True)
    format = models.CharField(max_length=30,null=True,blank=True)
    keywords = models.CharField(max_length=30,null=True,blank=True)
    citations = models.CharField(max_length=30,null=True,blank=True)
    host_department = models.CharField(max_length=30,null=True,blank=True)
    location = models.CharField(max_length=30,null=True,blank=True)
    number_of_files = models.IntegerField(default=0,null=True,blank=True)
    space = models.CharField(max_length=30,null=True,blank=True)
    retention_end_date = models.DateField('retention end date',null=True,blank=True)
    release_date = models.DateField('release date',null=True,blank=True)
    access_permission = models.CharField(max_length=30,null=True,blank=True)
    method_of_sharing = models.CharField(max_length=30,null=True,blank=True)
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
        widgets = { 
                   'start_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'end_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'coverage_start_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'coverage_end_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'retention_end_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'release_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'project' : forms.HiddenInput(),
                  }  
      

       
class ProjectForm(ModelForm):
    class Meta:
        model = Project        
        fields = ('id','name','principal', 'start_date', 'end_date', 'description',
                  'funding_source','funding_allocation','research_code')
        widgets = { 
                   'start_date': forms.DateInput(attrs={'class':'datepicker'}),
                   'end_date': forms.DateInput(attrs={'class':'datepicker'}),
                   
                  } 
    ## does not work  
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['principal'].widget.attrs['readonly'] = True
   
class ProjectMemberForm(ProjectForm):
        class Meta(ProjectForm.Meta):
            fields = ProjectForm.Meta.fields + ('member',)
    

    