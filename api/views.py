from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets

class taskViews(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()