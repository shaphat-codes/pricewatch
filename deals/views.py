from django.shortcuts import render
from . models import *
from . serializers import *
from . filters import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
# Create your views here.



# CATEGORY

@api_view(['POST'])
def CategoryCreate(request):
    #if request.user.is_landlord == True:

        if request.method == "POST":

            serializer = CategorySerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)

@api_view(['GET'])
def CategoryView(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)



# SUB-CATEGORY

@api_view(['POST'])
def SubcategoryCreate(request):
    #if request.user.is_landlord == True:

        if request.method == "POST":

            serializer = SubcategorySerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)

@api_view(['GET'])
def SubcategoryView(request):
    queryset = Subcategory.objects.all()
    serializer = SubcategorySerializer(queryset, many=True)
    return Response(serializer.data)



# COMPANY

@api_view(['POST'])
def CompanyCreate(request):
    #if request.user.is_landlord == True:

        if request.method == "POST":

            serializer = CompanySerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)

@api_view(['GET'])
def CompanyView(request):
    queryset = Company.objects.all()
    serializer = CompanySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BroadbandView(request):
    queryset = Broadband.objects.all()
    filterset = BroadbandFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = BroadbandSerializer(queryset, many=True)
    return Response(serializer.data)



