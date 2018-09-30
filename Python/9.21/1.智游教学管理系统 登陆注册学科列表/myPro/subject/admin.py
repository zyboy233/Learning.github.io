from django.contrib import admin
from subject.models import SubjectModel,SubjectAdminModel
# Register your models here.

admin.site.register(SubjectModel,SubjectAdminModel)