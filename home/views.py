#ws://localhost:8000/ws/test/
from django.shortcuts import render
import time
from asgiref.sync import async_to_sync
from channels.layers import  get_channel_layer
import json

# Create your views here.
def home(request):
    for i in range(1,10):
        channel_layer = get_channel_layer()
        data = {'count': i}
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group', {
                'type' : 'send_notification',
                'value' : json.dumps(data)
            })
        time.sleep(1)
    return render(request, 'home.html')
