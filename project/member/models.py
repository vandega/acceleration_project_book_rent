from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='images', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='member_groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='member_permissions',
    )

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

