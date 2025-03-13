from django.contrib import admin
from .models import *

# Register your models here.
class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1  # Number of extra forms to display

class ProjectAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline]
    list_display = ('Project_name', 'Company', 'year')
    search_fields = ('Project_name', 'Company')
    
admin.site.register(Project, ProjectAdmin)