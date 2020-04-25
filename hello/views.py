#
# Filename: views.py
# Project : Clock My Time
#
# Created by Tu Tong on 04/12/20
# Copyright 2020 Tu Tong. All rights reserved.
#
# https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from hello.models import Schedule
from hello.serializers import ScheduleSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

# https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({ "csrftoken": csrf.get_token(request) }, status=200)

@login_required()
def schedule_list(request):

    if request.method == 'GET':
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScheduleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

@login_required()
@ensure_csrf_cookie
def schedule_detail(request, pk):
    '''
    Retrieve, update or delete a schedule
    '''

    try:
        schedule = Schedule.objects.get(pk=pk)
    except Schedule.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = ScheduleSerializer(schedule)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ScheduleSerializer(schedule, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        schedule.delete()
        return HttpResponse(status=204)

@login_required(login_url="/login/")
def get_profile(request):
    user = request.user
    #user = User.objects.get(email=request.user.email)
    if user.first_name and user.last_name:
        fullname = user.first_name + " " + user.last_name
    else:
        fullname = user.username

    return JsonResponse({
            'fullname': fullname,
            'username': user.username,
            'email': user.email
        }, status=200)

def auth_login(request):
    return HttpResponse(status=401)


@csrf_exempt
def auth_logout(request):
    logout(request)
    return HttpResponse(status=200)