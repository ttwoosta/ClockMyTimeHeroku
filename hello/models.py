#
# Filename: models.py
# Project : Clock My Time
#
# Created by Tu Tong on 04/12/20
# Copyright 2020 Tu Tong. All rights reserved.
#

from django.db import models
from django.contrib.auth.models import User
from datetime import time, timedelta

class Schedule(models.Model):
    
    date = models.DateField("Date of the schedule")
    timeIn = models.TimeField("The time of clock in")
    timeOut = models.TimeField("The time of clock out")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["date"]

class PayCheck:

    def __init__(self, user, schedules):
        self.user = user
        items = []
        total = 0.0

        for s in schedules:
            items.append(PayCheckItem(s.id, s.user_id, s.date, s.timeIn, s.timeOut, 15.75))
        
        for i in items:
            total += i.total

        self.items = items
        self.total = total

class PayCheckItem:

    # date: models.DateField
    # timeIn: models.TimeField
    # timeOut: models.TimeField

    # base_rate = 0.0k
    # total = 0.0

    def __init__(self, schedule_id, user_id, date, timeIn, timeOut, base_rate):
        self.schedule_id = schedule_id
        self.user_id = user_id
        self.date = date
        
        # calculate hours
        td1 = timedelta(hours=timeIn.hour, minutes=timeIn.minute, seconds=timeIn.second)
        td2 = timedelta(hours=timeOut.hour, minutes=timeOut.minute, seconds=timeOut.second)
        delta = td2 - td1
        total_hours = delta.total_seconds() / 3600.00
        
        self.timeIn = timeIn.strftime("%I:%M %p")
        self.timeOut = timeOut.strftime("%I:%M %p")
        self.hours = total_hours
        self.base_rate = base_rate
        self.total = base_rate * total_hours
