from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TaskView

router = DefaultRouter()

router.register("task", TaskView, basename="task")


urlpatterns = [
    path('', include(router.urls))
]
