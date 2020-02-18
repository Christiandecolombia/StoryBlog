from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

import datetime
import re 

class Storymanager(models.Manager):
    def story_validator(self, postData):
        errors= {}
        if len(postData[''])<2:
            errors['mainbody']='Can not be empty'
        return errors

class Story(models.Model):
    title = models.CharField(max_length=25)
    mainbody = models.TextField()
    pubDate = datetime.datetime.now()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = Storymanager()
