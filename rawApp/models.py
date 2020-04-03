from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

# class User(models.Model):
#     id=models.AutoField(primary_key=True)
#     email = models.EmailField()
#     userName = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.userName
#
#
# class UserDetail(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     firstName= models.CharField(max_length=100,default=" ")
#     LastName = models.CharField(max_length=100, blank=True, default=" ")
#     photo = models.ImageField(upload_to='uploads/',default=" ")
#     company = models.CharField(max_length=1000,default=" ")
#     degisnation = models.CharField(max_length=500,default=" ")
#     date_of_birth = models.DateField(null=True)
#

class User(AbstractUser):

    email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.CharField(null=True,max_length=15)

    REQUIRED_FIELDS = ['username','phone','first_name',
                       'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
