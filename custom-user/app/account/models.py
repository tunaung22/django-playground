from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from .manager import UserManager


class User(AbstractBaseUser):
    user_uuid = models.UUIDField('User UUID',
                                 default=uuid4,
                                 editable=False)
    username = models.CharField('Username',
                                max_length=20,
                                unique=True)
    email = models.EmailField('Email',
                              unique=True)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField('Date joined',
                                       default=timezone.now)
    is_active = models.BooleanField('Is active',
                                    default=True)
    is_admin = models.BooleanField('Is admin',
                                   default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
