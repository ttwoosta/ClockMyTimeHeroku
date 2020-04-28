#
# Filename: serializers.py
# Project : Clock My Time
#
# Created by Tu Tong on 04/12/20
# Copyright 2020 Tu Tong. All rights reserved.
#
# https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers

from django.db import models
from rest_framework import serializers
from hello.models import Schedule

class ScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.DateField(required=True)
    timeIn = serializers.TimeField(required=False)
    timeOut = serializers.TimeField(required=False)

    user_id = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Schedule` instance, given the validated data.
        """
        return Schedule.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Schedule` instance, given the validated data.
        """
        instance.date = validated_data.get('date', instance.date)
        instance.timeIn = validated_data.get('timeIn', instance.timeIn)
        instance.timeOut = validated_data.get('timeOut', instance.timeOut)
        instance.save()
        return instance

class PayCheckItemSerializer(serializers.Serializer):
    schedule_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    date = serializers.DateField(required=True)
    timeIn = serializers.CharField()
    timeOut = serializers.CharField()
    hours = serializers.DecimalField(max_digits=5, decimal_places=2)
    base_rate = serializers.DecimalField(required=True, max_digits=5, decimal_places=2)
    total = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)

class PayCheckSerializer(serializers.Serializer):

    user_id = serializers.IntegerField(required=True, source='user.id')
    email = serializers.EmailField(source='user.email')

    items = PayCheckItemSerializer(many=True)
    total = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)



    