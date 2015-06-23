from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic

from dmpapp.models import Dataset, DatasetForm
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
    
    
    def get_queryset(self):
        project_id = self.request.GET.get("pid")
        return Dataset.objects.filter(project__id=project_id).filter(
                                      project__member__name=self.request.user)  
        
class DatasetDetailView(LoggedInMixin,generic.DetailView):
    
    model = Dataset
    template_name = 'dmpapp/datasetdetail.html'
    context_object_name = 'ds'
    
    def get_queryset(self):
        return Dataset.objects.filter(project__member__name=self.request.user)
  
    def postDS(self):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(self.request, self.template_name, {'form': form})


def update_ds(request,pk):
    
    form = DatasetForm(request.GET)
    
    # this is the GET method
    if request.method == 'GET':
        print("update_ds")
        ds = Dataset.objects.get(id=pk)
        print(ds)
        form = DatasetForm(instance=ds)

    return render(request, 'dmpapp/updateds.html', {'form': form})


def update_dspost(request):
    print("update_dspost")
        
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DatasetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            project = data['project']
            project_id = str(project.id)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dmp/datasets/?pid=' + project_id)
        else:
            print(form.errors) #To see the form errors in the console. 
    
    return render(request, 'dmpapp/updateds.html', {'form': form})

