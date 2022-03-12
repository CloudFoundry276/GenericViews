from django.shortcuts import render
from gvApp.models import Student
from gvApp.serializers import StudentSerializer
from rest_framework import generics


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
