from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TaskView, HashtagView, VideoView, FeedbackList, FeedbackDetail

router = DefaultRouter()

router.register("task", TaskView, basename="task")
# router.register("feedback", FeedbackView, basename="feedback")
router.register("hashtag", HashtagView, basename="hashtag")
router.register("video", VideoView, basename="video")


urlpatterns = [
    path('', include(router.urls)),
    path("feedback/", FeedbackList.as_view(), name="feedback_list"),
    path("feedback/<int:pk>/", FeedbackDetail.as_view(), name="feedback_detail")
]
