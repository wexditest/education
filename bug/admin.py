from django.contrib import admin
from .models import BugList



class BugListAdmin(admin.ModelAdmin):
    list_display = ['bug_title','dev_team','status']



# Register your models here.
admin.site.register(BugList, BugListAdmin)
