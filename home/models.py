from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from channels.layers import  get_channel_layer
from asgiref.sync import async_to_sync
import json

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=100)
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        notification_objs = Notification.objects.filter(is_seen = False).count()
        data = {'count' : notification_objs, 'current_notification' : self.notification}
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type' : 'send_notification',
                'value' : json.dumps(data)
            })
        super(Notification, self).save(*args, **kwargs)
