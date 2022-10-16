from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length = 200,null = False)
    last_name = models.CharField(max_length = 200,null = False)
    email = models.EmailField(unique=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    country = models.CharField(max_length = 250,blank=True)

    def officer(self):
        Profile.is_officer = True
        Profile.save(self,update_fields=None)
        return Profile

    def admin(self):
        Profile.is_admin = True
        Profile.save(self,update_fields=None)
        return Profile

    def __str__(self):
        return self.user.name