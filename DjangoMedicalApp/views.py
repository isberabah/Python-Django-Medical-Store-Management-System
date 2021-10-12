from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.templatetags.rest_framework import data
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from DjangoMedicalApp.models import Company
from DjangoMedicalApp.serializer import CompanySerializer


class CompanyViewSets(viewsets.ViewSet) :
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self , request) :
        company = Company.object.all()
        serializer = CompanySerializer(company , many=True , context={ "request" , request })
        response_dict = { "error" : False , "message" : "All Company List Data" , "data" : serializer.data }
        return Response(response_dict)

    def create(self , request) :
        try :
            serializer = CompanySerializer(data=request.data , context=("request" , request))
            serializer.is_valid()
            serializer.save()
            response_dict = { "error" : False, "message": "Company Data save Successfully"}
        except :
            response_dict = { "error" : True, "message": "Error during creating Company Data"}
        return Response(response_dict)

    def update(self, request,pk=None):
        try:
            queryset=Company.object.all()
            company=get_object_or_404(queryset,pk=pk)
            serializer = CompanySerializer(company, data=request.data , context=("request" , request))
            serializer.is_valid()
            serializer.save()
            response_dict = { "error" : False, "message": "Successfully Updated Company Data"}
        except:
            response_dict = { "error" : True, "message": "Error During Updatin Company Data"}
        return Response(response_dict)



company_list = CompanyViewSets.as_view({ "get" : "list" })
company_create = CompanyViewSets.as_view({ "post" : "create" })
company_update = CompanyViewSets.as_view({ "post" : "update" })
