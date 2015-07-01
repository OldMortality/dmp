from _overlapped import NULL

from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from dmpapp.models import Dataset, DatasetForm, ProjectForm
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
        return Project.objects.filter(member__name=self.request.user)
        #return Project.objects.all()
        #return project_list = Project.objects.filter(name__startswith=this_email)
     
    #request.session['email']="Dinosaurs"
    #this_email = request.session.get('email')
    #context = RequestContext(request, {
    #    'project_list': project_list,
    
    #return HttpResponse(template.render(context))
    
class ProjectDetailView(LoggedInMixin,generic.DetailView):
    
    model = Project
    template_name = 'dmpapp/projectdetail.html'
    def get_queryset(self):
        return Project.objects.filter(member__name=self.request.user)
  
class DatasetView(LoggedInMixin,generic.ListView):
    
    model = Dataset
    template_name = 'dmpapp/datasetlist.html'
    context_object_name = 'dataset_list'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DatasetView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['project_id'] = self.request.GET.get("pid")
        return context
    
    def get_queryset(self):
        project_id = self.request.GET.get("pid")
        return Dataset.objects.filter(project__id=project_id).filter(
                                      project__member__name=self.request.user)  
        



@login_required
def project_detail_new(request):
    
    print("project_detail_new")
    form = ProjectForm()
    return render(request,'dmpapp/update_project.html', {'form': form})

@login_required
def project_detail_get(request,pk):
    
    print("project_detail_get")
    project = Project.objects.get(id=pk)
    # save project to the context
    request.session['project_id']=pk
    form = ProjectForm(instance=project)
    form.id = project.id
    return render(request,'dmpapp/update_project.html', {'form': form})
    
@login_required
def project_detail_post(request,pk=None):
    
    print("project_detail_post")
     
        
    if pk is not None:
        print("!!existing project")
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
def update_ds(request,pk=None):
    
    print("update_ds")
    print(request.method)
    if pk is not None:
        
        print("a")
        ds = Dataset.objects.get(id=pk)
        print("id is " + pk)
        form = DatasetForm(instance=ds)
        form.id = ds.id
    else:
        print("b")  
        # get project from the session
        this_project_id = request.session.get('project_id')
        print("the current project is")
        print(this_project_id)
        
        
        ds = None
        form = DatasetForm()
        form.project = Project.objects.get(id=this_project_id)
      
    if request.method == 'GET':
        print("method = GET")
        return render(request,'dmpapp/updateds.html', {'form': form})
    if request.method == 'POST':
        print("posting dataset")
        form = DatasetForm(request.POST,instance=ds)
        
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            project = data['project']
            project_id = str(project.id)
            form.save(commit=False)
            form.project = Project.objects.get(id=this_project_id)
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

@login_required
def dataset_get(request,pk):
    
    print("dataset_get")
    print(request.method)
    ds = Dataset.objects.get(id=pk)
    print("id is " + pk)
    form = DatasetForm(instance=ds)
    form.id = ds.id
    return render(request,'dmpapp/updateds.html', {'form': form})
    
        


def dataset_new(request):
    
    print("new dataset")  
    # get project from the session
    this_project_id = request.GET.get('project_id')
    print("the current project is")
    print(this_project_id) 
        
    ds = None
    form = DatasetForm()
    form.project = Project.objects.get(id=this_project_id)
      
    return render(request,'dmpapp/updateds.html', {'form': form})
    
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