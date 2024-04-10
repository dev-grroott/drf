from django.contrib import admin
from todo.models import Task, Feedback, Hashtag, Video

admin.site.register([Task, Feedback, Hashtag, Video])
