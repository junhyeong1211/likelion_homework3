from rest_framework import serializers
from .models import Todo

class TodosimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','complete','important')
        
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','description','created','complete','important')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','description','important')
