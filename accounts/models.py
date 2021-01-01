from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, commit=True):

        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)

        if commit:
            user.save()

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password, commit=False)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100, blank=False)
    
    is_admin = models.BooleanField('admin status', default=False)
    is_staff = models.BooleanField('staff status', default=False)
    is_superuser = models.BooleanField('superuser status', default=False)
    is_active = models.BooleanField('active', default=True)
    
    date_joined = models.DateTimeField(auto_now=True, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
  
    def has_module_perms(self, app_label):
        return True
