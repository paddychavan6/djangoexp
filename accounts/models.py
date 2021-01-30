from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator
import os
from uuid import uuid4

def nameimage(instance,filename):
    upload_to='upload'
    ext=filename.split(".")[-1]
    if instance.pk:
        filename='{}.{}'.format(instance.pk,ext)
    else:
        filename=filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(upload_to,filename)

class Myaccountmanager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
             raise ValueError("user must have email")
        if not username:
             raise ValueError("user must have username")

        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_active=True
        user.is_admin=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    firstname       =models.CharField(max_length=20)
    lastname        =models.CharField(max_length=30)
    username        =models.CharField(max_length=30,unique=True)
    email           =models.EmailField(verbose_name='email',max_length=60,unique=True)
    phone_regex     =RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobno           =models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    voterID         =models.CharField(max_length=15)
    address         =models.CharField(max_length=40)
    zipcode         =models.CharField(max_length=7)
    age             =models.CharField(max_length=3)
    image           =models.ImageField(upload_to='upload/')
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_superuser    =models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=Myaccountmanager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True



class logimage(models.Model):
    vid=models.CharField(max_length=10)
    limage=models.ImageField(upload_to="logupload/")

class modelfile(models.Model):
    bjp=models.FileField(upload_to="votes/")
    mns=models.FileField(upload_to="votes/")
    congress=models.FileField(upload_to="votes/")