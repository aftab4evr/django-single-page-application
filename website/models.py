# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


GENDERTYPE=(
    ("Male", "Male"),
    ("Female", "Female"),
)

class UserManagement(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    gender = models.CharField(
        "Gender", max_length=20, default='Male', choices=GENDERTYPE)
 
    name = models.CharField('Name', max_length=256,)
    email = models.EmailField("Email Address", null=True, unique=True, blank=True, error_messages={
                              'unique': "This email id is already registered."})
    mobile = models.CharField('Mobile Number', max_length=15, unique=True, null=True,
                              blank=True, error_messages={'unique': "This mobile no is already registered."})
    
    pass
