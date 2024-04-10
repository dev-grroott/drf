from rest_framework import viewsets
from todo.models import Task, Feedback, Hashtag, Video
from todo.serializer import TaskSerializer, FeedbackSerializer, HashtagSerializer, VideoSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


def home(request):
    pass


class CustomTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class FeedbackView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]


class HashtagView(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = [CustomTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "delete", "patch"]