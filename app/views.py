from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def course_apiview(request):
    if request.method=="GET":
        courses=Courses.objects.all()
        serializer=CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    
    