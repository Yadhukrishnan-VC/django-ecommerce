from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

#-----------------------------------
#     UserTable
#------------------------------------
class UserTable(AbstractUser):
    is_admin = models.BooleanField(default=False)
    country_code = models.CharField(max_length=5, null=True,default='')
    date_of_birth = models.DateField(blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='user_table_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_table_user_permissions', blank=True)