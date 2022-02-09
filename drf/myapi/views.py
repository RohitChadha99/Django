from functools import partial
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    # if request.method == 'GET':
    #     return Response({'msg':'HEllo!!!'})

    # if request.method == 'POST':
    #     return Response({'msg':'HEllo from POST !!!'})

    if request.method == 'GET':
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu , many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data saved'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data updated !!'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data completely updated !!'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg': 'Data Deleted !!'})

