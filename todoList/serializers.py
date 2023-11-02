
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TodoItem

# class TodoItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TodoItem
        
#         fields = '__all__'
        
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'username', 'email']


class TodoItemSerializer(serializers.ModelSerializer):
    # user = UserSerializer()  # Use the UserSerializer to serialize the user field

    class Meta:
        model = TodoItem
        fields = ('id', 'user', 'title', 'completed')