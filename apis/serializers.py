# get data from models --> json

from rest_framework import serializers
from todolist import models


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.List
        fields = '__all__'

'''
        fields = (
            'id',
            'item',
            'completed',
        )
'''