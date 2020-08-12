from rest_framework import serializers

from .models import Task,TaskTracker
import time
from datetime import datetime


class MemberSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		
		date=serializers.DateField("%d %b, %Y")
		integer=serializers.IntegerField(min_value=1, max_value=4)
		
		model = TaskTracker
		fields = ('task_type','update_type','email')