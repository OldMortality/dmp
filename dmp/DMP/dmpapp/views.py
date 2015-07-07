from _overlapped import NULL

from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from dmpapp.models import Dataset, DatasetForm, ProjectForm, Person,\
    ProjectMemberForm
from dmpapp.models import Project


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

# Create your views here.

class IndexView(LoggedInMixin,generic.ListView):
    
    model = Project
    template_name = 'dmpapp/index.html'
    context_object_name = 'project_list'
    
    
    
    
    def get_queryset(self):
        user_name = self.request.user
       
        # get the email address for the current user
        # this will need to come from SAML later on. 
        this_person = Person.objects.filter(name= user_name)[:1]
        if (this_person.count() > 0):
            email = this_person[0].email
        print(email)
        # store it in the session
        self.request.session['email']=email
    
        
        print("getting the projects" )
        print(self.request.user)
        #projects = Project.objects.filter(member__name=self.request.user).order_by('name')
        projects = Project.objects.filter(member__email=email).order_by('name')
        print("found this many projects: " + str(projects.count()))
        
        return projects
        #return Project.objects.all()
        #return project_list = Project.objects.filter(name__startswith=this_email)
     
    #request.session['email']="Dinosaurs"
    #this_email = request.session.get('email')
    #context = RequestContext(request, {
    #    'project_list': project_list,
    
    #return HttpResponse(template.render(context))
    
class ProjectDetailView(LoggedInMixin,generic.DetailView):
    
    ##
    ## Get email address for the current user, and store this in the session
     
    ##this_person = Person.objects.filter(name = request.user)
    #print("this person has email address " + this_person.email)
    
    model = Project
    template_name = 'dmpapp/projectdetail.html'
    def get_queryset(self):
        return Project.objects.filter(member__name=self.request.user)
  
class DatasetView(LoggedInMixin,generic.ListView):
    
    model = Dataset
    template_name = "dmpapp/datasetlist.html"
    context_object_name = "dataset_list"
    
    def get_queryset(self):
        print("getting the projects")
        project_id = self.request.GET.get("pid")
        return Dataset.objects.filter(project__id=project_id).filter(
                                      project__member__name=self.request.user)  

    
    def get_context_data(self, **kwargs):
        context = super(DatasetView, self).get_context_data(**kwargs)
        context['project_id'] = self.request.GET.get("pid")
        return context
    
            



@login_required
def project_new(request):
    
    print("project_new")
    form = ProjectForm()
    return render(request,'dmpapp/update_project.html', {'form': form})

@login_required
def project_get(request,pk):
    
    print("project_get")
    if check_user_in_project(request,pk)==0:
            return HttpResponseRedirect('/dmp/')  
       
    project = Project.objects.get(id=pk)
    # save project to the context
    #request.session['project_id']=pk
    
    # Show the members only if current user is the principal investigator
    # for this project.
    if (project.principal.email == request.session.get('email')):
        print("user is the principal")
        form = ProjectMemberForm(instance=project)
    else: 
        print("user is not the principal")
        print(project.principal.email)
        print(request.user.email)
        form = ProjectForm(instance=project)
    
    form.id = project.id
    return render(request,'dmpapp/update_project.html', {'form': form})
    
@login_required
def project_post(request,pk=None):
    
    print("project_post")
     
        
    if pk is not None:
        print("existing project")
        if check_user_in_project(request,pk)==0:
            return HttpResponseRedirect('/dmp/')  
       
        # existing project
        project = Project.objects.get(id=pk)
        # save project to the context
        request.session['project_id']=pk
        form = ProjectForm(request.POST,instance=project)
        form.id = project.id
    
    else:
        print("!!new project") 
        # new project
        project = None
        form = ProjectForm()
        form = ProjectForm(request.POST,instance=project)
        #print(form)
        # check whether it's valid:
    
    if form.is_valid():
        print("form is valid")
        data = form.cleaned_data
        project_members = data['member']
        # to do: make this into a validator
        x = project_members.filter(name=request.user)
        if not x:
            print("current user not in the members")
        else:   
            form.save()
            print("update done xx")
        
        #  process the data in form.cleaned_data as required
        return HttpResponseRedirect('/dmp')
    else:
        print("form errors")
        print(form.errors) #To see the form errors in the console. 
        return render(request, 'dmpapp/update_project.html', {'form':form})




@login_required
def dataset_get(request,pk):
    
    print("dataset_get")
    print(request.method)
    ds = Dataset.objects.get(id=pk)
    print("id is " + pk)
    
    project_id = ds.project.id
    print("project id is " + str(project_id))
    
    this_project = Project.objects.get(id=project_id)
    print("this project: " + this_project.name)
    form = DatasetForm(instance=ds)
    form.project = this_project
    
    #xxx
    form.id = ds.id
    return render(request,'dmpapp/updateds.html', {'form': form, 'pid':project_id})
    
        


def dataset_new(request):
    
    print("new dataset")  
    # get project from the session
    this_project_id = request.GET.get('project_id')
    print("the current project is")
    print(this_project_id) 
    
    if check_user_in_project(request,this_project_id)==0:
        return HttpResponseRedirect('/dmp/')  
       
    
    pr = Project.objects.get(id=this_project_id)
    print("pr_id " + str(pr.id))
    data = {'name': "New"  ,'project': pr.id, 'owner': request.user.id}
    
    form = DatasetForm(data)
      
    return render(request,'dmpapp/updateds.html', {'form': form, 'pid':this_project_id})

def check_user_in_project(request,pid):
    print("check that user is in project")  
    email = request.session['email']
    print("email:" + email)
    qs = Project.objects.filter(id=pid).filter(member__email=email)
    if not qs:
        print("current user not in the members") 
        return(0)   
    else:
        print("current user is a member of this project")
        return(1)
      
@login_required
def dataset_post(request,pk=None):
    
    print("dataset_post")
    if pk is not None:
        print("existing dataset")
        ds = Dataset.objects.get(id=pk)
        print("id is " + pk)
        form = DatasetForm(instance=ds)
        form.id = ds.id
    else:
        print("new dataset")  
        # get project from the session
        ds = None
        form = DatasetForm()
        
    print("posting dataset")
    form = DatasetForm(request.POST,instance=ds)
        
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        project = data['project']
        project_id = str(project.id)
        
        if check_user_in_project(request,project_id)==0:
            return HttpResponseRedirect('/dmp/')  
        # check that current user is a member of this project
        
        form.save(commit=False)
        form.save()
        print("no errors. redirecting to dmp/datasets/?pid")
        #  process the data in form.cleaned_data as required
        return HttpResponseRedirect('/dmp/datasets/?pid=' + project_id)
    else:
        print("form errors in else:")
        print(form.errors) #To see the form errors in the console. 
        #return HttpResponseRedirect('/dmp/updateds/' + str(ds.id)+'/')
        form.id = pk
        return render(request, 'dmpapp/updateds.html', {'form':form})




def dataset_del(request,pk):
    
    project_id = request.GET.get('project_id')
    if check_user_in_project(request,project_id)==0:
        return HttpResponseRedirect('/dmp/')  
       
    print("remove dataset" )
    print(pk)
    print(project_id)  
    # get project from the session
    this_dataset = Dataset.objects.get(id=pk)
    this_dataset.delete()
    return HttpResponseRedirect('/dmp/datasets/?pid=' + project_id)
    

#@login_required
#def update_dspost(request):
#    print("update_dspost")
        
    # if this is a POST request we need to process the form data
         
        # create a form instance and populate it with data from the request:
#    form = DatasetForm(request.POST)
##    print(form)
# check whether it's valid:
#   if form.is_valid():
#       data = form.cleaned_data
#       project = data['project']
#       project_id = str(project.id)
#       form.save()
        
        #  process the data in form.cleaned_data as required
#      return HttpResponseRedirect('/dmp/datasets/?pid=' + project_id)
#  else:
#     print(form.errors) #To see the form errors in the console. 
#
#    return render(request, 'dmpapp/updateds.html', {'form': form})