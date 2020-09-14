# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .forms import AddUserForm
from .models import UserManagement
from .string_to_html.viewpage import getViewDetailPage
from .string_to_html.editpage import getEditRecordPage
from .string_to_html.addpage import getAddRecordPage
from .string_to_html.dashboardpage import getDashboardPage
from .serializers import AddRecordSerializer



class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


class DeleteRecordView(View):
    def get(self, request,uuid):
        UserManagement.objects.filter(uuid=uuid).delete()
        return HttpResponse(status=200)


class GetRecordView(View):
    def get(self,request):
        queary = UserManagement.objects.all().order_by('-id')
        # paginator = Paginator(queary, 10)
        # page=1
        # try:
        #     queary = paginator.page(page)
        # except PageNotAnInteger:
        #     queary = paginator.page(1)
        # except EmptyPage:
        #     queary = paginator.page(paginator.num_pages)
        data = getDashboardPage(queary)
        return JsonResponse({'data':data})


class AddRecordView(View):
    def post(self,request):
        print(request.POST)
        params = request.POST
        if UserManagement.objects.filter(email=params['email']) or UserManagement.objects.filter(mobile=params['mobile']):
            return JsonResponse({'response_message':'Email or phone no exist.'},status=400)
        user_form = AddUserForm(request.POST)   
        if user_form.is_valid():
            user_form.save()
            return JsonResponse({})
        # serializer = AddRecordSerializer(data=params)
        # serializer.is_valid()
        # serializer.save()
        # return JsonResponse({})

class EditRecordView(APIView):
    def post(self,request):
        params = request.data
        user = UserManagement.objects.get(uuid=params['uuid'])
        serializer = AddRecordSerializer(instance=user,data=params,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({})

class GetAddRecordPage(View):
    def get(self,request):
        data = getAddRecordPage()
        return JsonResponse({'data':data})

class GetEditRecordPage(View):
    def get(self,request,uuid):
        user = UserManagement.objects.get(uuid=uuid)
        data = getEditRecordPage(user)
        return JsonResponse({'data':data})

class GetViewRecordView(View):
    def get(self,request,uuid):
        user = UserManagement.objects.get(uuid=uuid)
        data = getViewDetailPage(user)
        return JsonResponse({'data':data})


class HandelAnyUrl(View):
    def get(self,request):        
        return render(request,'index.html')