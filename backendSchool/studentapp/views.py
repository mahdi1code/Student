from django.shortcuts import render
from .models import student
from .Serializers import studentSerializers
from rest_framework import viewsets

# Create your views here.
def welcome(request):
    return render(request=request,template_name="student.html")

class studentviewset(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentSerializers
