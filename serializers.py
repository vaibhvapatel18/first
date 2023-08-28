from rest_framework import serializers
from api.models import Student

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fileds = ['id','name','roll']