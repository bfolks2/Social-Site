from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    #Attributes for User are built in to the auth.models.User

    def __str__(self):
        return "@{}".format(self.username) #username is a built in attribute from auth.models.User
