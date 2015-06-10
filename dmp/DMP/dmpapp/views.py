from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.context import RequestContext

from dmpapp.models import Project


# Create your views here.
def index(request):
    project_list = Project.objects.all()
    template = loader.get_template('dmpapp/index.html')
    context = RequestContext(request, {
        'project_list': project_list,
    })
    return HttpResponse(template.render(context))