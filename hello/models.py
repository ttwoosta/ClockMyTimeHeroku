#
# Filename: models.py
# Project : Clock My Time
#
# Created by Tu Tong on 04/12/20
# Copyright 2020 Tu Tong. All rights reserved.
#

from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    
    date = models.DateField("Date of the schedule")
    timeIn = models.TimeField("The time of clock in")
    timeOut = models.TimeField("The time of clock out")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]