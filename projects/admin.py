from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',               {'fields': ['title']}),
        ('Description',         {'fields': ['description']}),
        ('Technology',          {'fields': ['technology']}),
        ('Image',               {'fields': ['image']})
    ]

admin.site.register(Project, ProjectAdmin)    