from django.contrib import admin

from dmpapp.models import Dataset
from dmpapp.models import Project
from dmpapp.models import Ethics_Document
from dmpapp.models import Person




# Register your models here.
admin.site.register(Dataset)
admin.site.register(Project)
admin.site.register(Ethics_Document)
admin.site.register(Person)

