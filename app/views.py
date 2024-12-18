from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status

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

@api_view(['GET', 'PUT', 'DELETE'])
def course_detailview(request,pk):
    try:
        course=Courses.objects.get(pk=pk)
    except Courses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    elif request.method=='DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
