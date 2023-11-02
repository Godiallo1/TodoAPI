from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from django.contrib.auth.models import User
from .models import TodoItem


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userlist(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        tasks = User.objects.filter(Q(username__icontains=query))
        serializer = UserSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tasklist(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        tasks = TodoItem.objects.filter(Q(title__icontains=query))
        serializer = TodoItemSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def taskdetail(request, pk):
    try:
        task_detail = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response({"detail": "Todo Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        serializer = TodoItemSerializer(task_detail, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = TodoItemSerializer(task_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        serializer = TodoItemSerializer(task_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = TodoItemSerializer(task_detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task_detail.delete()
        return Response({"detail": "Todo Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        