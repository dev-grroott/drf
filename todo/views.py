from rest_framework import viewsets
from todo.models import Task
from todo.serializer import TaskSerializer


def home(request):
    pass


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ["get", "post", "put", "delete"]

