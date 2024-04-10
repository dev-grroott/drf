from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TaskView, FeedbackView, HashtagView, VideoView

router = DefaultRouter()

router.register("task", TaskView, basename="task")
router.register("feedback", FeedbackView, basename="feedback")
router.register("hashtag", HashtagView, basename="hashtag")
router.register("video", VideoView, basename="video")


urlpatterns = [
    path('', include(router.urls))
]
