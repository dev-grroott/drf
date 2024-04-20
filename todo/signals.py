from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver

from todo.models import Preference


@receiver(post_save, sender=User)
def create_preference(sender, instance, created, **kwargs):
    if created:
        Preference.objects.create(user=instance, dp="everyone") # insert into table () values ()


