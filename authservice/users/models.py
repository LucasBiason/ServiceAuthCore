from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Create and saves the new user """
        if not email:
            raise ValueError("User must have email address")
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """ Create and saves the new superuser """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user models that suppors using email instead of username """
    
    email = models.EmailField(
        'E-mail', 
        unique=True, blank=False
    )

    is_active = models.BooleanField(
        'Active', default=True
    )

    is_staff = models.BooleanField(
        'Staff', default=False
    )

    is_superuser = models.BooleanField(
        'Super User', default=False
    )

    first_name = models.CharField(
        'First Name', 
        max_length=30, 
        default=''
    )

    last_name = models.CharField(
        'Last Name', 
        max_length=30, 
        default=''
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'