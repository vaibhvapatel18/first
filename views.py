from django.shortcuts import render
from .serializers import Studentserializer
from .models  import Student
from rest_framework.generics import ListAPIView
from .mypage import Page
# Create your views here.
class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    pagination_class = Page
