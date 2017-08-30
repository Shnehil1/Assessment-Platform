from django.contrib import admin
from .models import Assignment, Assestment, UserProfile, Document


#register your models here
admin.site.register(Assignment)
admin.site.register(Assestment)
admin.site.register(UserProfile)
admin.site.register(Document)


