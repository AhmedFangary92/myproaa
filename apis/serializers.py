# get data from models --> json

from rest_framework import serializers
from todolist.models import List


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'item',
            'completed',
        )
        model = List
        # fields = '__all__'
