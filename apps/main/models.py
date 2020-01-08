from __future__ import unicode_literals
from django.db import models

import datetime
import re 

# This is the user model. Regex for creating accounts

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usermanager(models.Manager):
    def register_validator(self, postData):
        errors= {}
        if len(postData['firstName'])<2:
            errors['firstName']='first name needed'
        if len(postData['lastName'])<2:
            errors['lastName']='last name needed'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='email required'
        if len(postData['password'])<8:
            errors['password']='password to short'
        if re.search('[A-Z]',postData['password']) is None:
            errors['password']='password needs one capital letter'
        if postData['password']!=postData['conpassword']:
            errors['password']="passwords dont match"
        return errors

    def login_validator(self, postData):
        errors={}
        try: #try to see if this is there.
            user = User.objects.get(email=postData['logemail'])
            if user.password == postData['logpassword']: # If this conditional returns true
                return errors #then do this
            else: #otherwise
                errors['logpassword'] = "Password is wrong"
                return errors
        except: #if you tried and failed. Quit      
            errors['logemail'] = "This email is invalid"
            return errors

class Storymanager(models.Manager):
    def validator(self, postData):
        errors= {}
        if len(postData[''])<2:
            errors['mainbody']='Can not be empty'
        return errors

class User(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=45)
    objects = Usermanager()


class Story(models.Model):
    title = models.CharField(max_length=25)
    mainbody = models.TextField()
    pubDate = datetime.datetime.now()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = Storymanager()
