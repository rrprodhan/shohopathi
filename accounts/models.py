from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    #Here auth.models.User gets the currently logged in user's Object and
    #permissionsMixin gives fields according to the objects access permissions
    def __str__(self):
        return "@{}".format(self.username)
