from rest_framework import viewsets
from todo.models import Task, Feedback, Hashtag, Video
from todo.serializer import TaskSerializer, FeedbackSerializer, HashtagSerializer, VideoSerializer, TaskSerializerDuplicate
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404


def home(request):
    pass


class CustomTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
        
    # def get_object(self):
    #     id = self.kwargs["pk"]
    #     return get_object_or_404(Task, id=int(id)+1, user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return TaskSerializer
        return TaskSerializerDuplicate

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class HashtagView(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]