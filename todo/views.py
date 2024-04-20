from rest_framework import viewsets
from todo.models import Task, Feedback, Hashtag, Video
from todo.serializer import TaskSerializer, FeedbackSerializer, HashtagSerializer, VideoSerializer, TaskSerializerDuplicate
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


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

# class FeedbackView(viewsets.ModelViewSet):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer
#     authentication_classes = [CustomTokenAuthentication, SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     http_method_names = ["get", "post", "put", "delete", "patch"]


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
    
class FeedbackList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeedbackDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id): # primay key
        try:
            return Feedback.objects.get(pk=id) # Feedback.objects.get(id=pk)  get() == 1 {}  filter()  any 0, 1, 1+ [] [{}] [{}{}{}{}]
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FeedbackSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)