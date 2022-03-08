from rest_framework import routers,serializers,viewsets
from .models import Task
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'first_name', 'last_name', 'e_mail','major','count','check_in_time']
        
    
    