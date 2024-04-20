from django.db import models

from django.contrib.auth.models import User

CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]

class Task(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "task"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Task, self).save(args, kwargs)

class Feedback(models.Model):
    rating = models.CharField(choices=CHOICES, max_length=5)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating} - {self.user}"
    
    class Meta:
        db_table = "feedback"

class Hashtag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "hashtag"

class Video(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "video"

class Preference(models.Model):
    dp = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "preference"

    def __str__(self):
        return f"{self.dp} - {self.user}"
