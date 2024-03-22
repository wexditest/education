from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ("Open", "Open"),
    ("In-Progress", "In-Progress"),
    ("Testing", "Testing"),
    ("Close", "Close"),

    )


class BugList(models.Model):
  bug_title = models.CharField(max_length=255)
  bug_desc = models.CharField(max_length=500)
  bug_file = models.FileField(upload_to = "bug_file/")
  dev_team = models.ForeignKey(User,on_delete=models.CASCADE,)
  status = models.CharField(max_length=19,choices=STATUS_CHOICES,default="Open")



