from django.contrib import admin
from todo.models import Task, Feedback, Hashtag, Video, Preference

admin.site.register([Task, Feedback, Hashtag, Video, Preference])
