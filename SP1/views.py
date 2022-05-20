from asyncio.windows_events import NULL
import imp
from re import X
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from numpy import empty
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SP1.models import Nutzer, Channel, Video
from SP1.serializers import NutzerSerializer, ChannelSerializer, VideoSerializer

# Create your views here.

@csrf_exempt
def NutzerApi(request,username=NULL):
    if request.method=='GET':
        nutzers = Nutzer.objects.filter(NutzerName=username)
        nutzers_serializer=NutzerSerializer(nutzers, many=True)
        return JsonResponse(nutzers_serializer.data, safe=False)
    elif request.method=='POST':
        nutzer_data=JSONParser().parse(request)
        nutzers_serializer=NutzerSerializer(data=nutzer_data)
        if nutzers_serializer.is_valid():
            nutzers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        nutzer_data=JSONParser().parse(request)
        nutzer=Nutzer.objects.get(NutzerName=nutzer_data['NutzerName'])
        nutzers_serializer=NutzerSerializer(nutzer,data=nutzer_data)
        if nutzers_serializer.is_valid():
            nutzers_serializer.save()
            return JsonResponse("Update Successful", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        nutzer=Nutzer.objects.get(NutzerName=username)
        nutzer.delete()
        return JsonResponse("Deleted Successfully", safe=False)

'''
def NutzerApiTest(request):
    cuser = request.user
    return cuser.NutzerName
    #username = request.username;
    #nutzers = Nutzer.objects.get(NutzerName=username)
    #nutzers_serializer=NutzerSerializer(nutzers, many=True)
    #return JsonResponse(nutzers_serializer.data, safe=False)
'''

@csrf_exempt
def userlogin(request):
    if request.method == "POST":
        #username = request.POST['NutzerName']
        #password = request.POST['NutzerPasswort']
        nutzer_data=JSONParser().parse(request)
        username = nutzer_data['NutzerName']
        password = nutzer_data['NutzerPasswort']
        #nutzernamedb = Nutzer.objects.get(NutzerName=nutzername)
        #nutzerpassdb = Nutzer.objects.get(NutzerPasswort=nutzerpasswort)
        user = authenticate(request, NutzerName=username, NutzerPasswort=password)
        if user is not None:
            return JsonResponse("Login Successful", safe=False)
        else:
            return JsonResponse("Login Unsuccessful", safe=False)
